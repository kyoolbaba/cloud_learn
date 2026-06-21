"""sample_app — a tiny FastAPI forecasting service to learn Docker with.

It stands in for your real db_polars_app.py: same shape (a web UI + JSON API that
runs a forecast), but with zero heavy ML deps so the Docker build is fast and
reliable. Every Docker concept you learn here applies 1:1 to the real app —
later you just swap this in for db_polars_app.py and add its requirements.

Endpoints:
  GET  /            -> minimal HTML UI (enter numbers, get a forecast chart)
  GET  /health      -> {"status": "ok"} for container health checks
  POST /api/forecast-> {"history":[...], "horizon":H, "method":"naive|ma|trend"}
  GET  /api/info    -> env + version (shows env vars passed via -e / compose)

Run locally (no Docker):  uvicorn app:app --host 0.0.0.0 --port 8011 --reload
"""
from __future__ import annotations

import os
import statistics
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Sample Forecast Service")

VERSION = os.environ.get("APP_VERSION", "0.1.0")
ENV_NAME = os.environ.get("APP_ENV", "local")           # set via -e APP_ENV=... or compose
DATA_DIR = os.environ.get("DATA_DIR", "/data")          # mounted as a volume in Docker


# ----- forecasting (pure python, no numpy needed) ---------------------------
def forecast(history: list[float], horizon: int, method: str) -> list[float]:
    if not history:
        return [0.0] * horizon
    if method == "naive":                      # repeat the last value
        return [float(history[-1])] * horizon
    if method == "ma":                         # moving average of last up-to-3 points
        window = history[-3:]
        avg = sum(window) / len(window)
        return [round(avg, 4)] * horizon
    if method == "trend":                      # fit a line y = a + b*t, extrapolate
        n = len(history)
        xs = list(range(n))
        mean_x = statistics.fmean(xs)
        mean_y = statistics.fmean(history)
        denom = sum((x - mean_x) ** 2 for x in xs) or 1.0
        b = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, history)) / denom
        a = mean_y - b * mean_x
        return [round(a + b * (n + h), 4) for h in range(horizon)]
    raise ValueError(f"unknown method: {method}")


class ForecastRequest(BaseModel):
    history: list[float]
    horizon: int = 6
    method: str = "trend"          # naive | ma | trend


@app.post("/api/forecast")
def api_forecast(req: ForecastRequest):
    yhat = forecast(req.history, req.horizon, req.method)
    return {"method": req.method, "horizon": req.horizon, "forecast": yhat}


@app.get("/health")
def health():
    return {"status": "ok", "version": VERSION}


@app.get("/api/info")
def info():
    # Proves how env vars and volumes flow into a container.
    data_exists = os.path.isdir(DATA_DIR)
    return {
        "version": VERSION,
        "env": ENV_NAME,
        "hostname": os.uname().nodename if hasattr(os, "uname") else "n/a",
        "data_dir": DATA_DIR,
        "data_dir_mounted": data_exists,
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!doctype html><html><head><title>Sample Forecast</title>
<style>body{font-family:system-ui;max-width:640px;margin:40px auto;padding:0 16px}
input,select,button{font-size:16px;padding:6px}#out{white-space:pre;background:#f4f4f4;padding:12px;border-radius:8px}</style>
</head><body>
<h2>Sample Forecast Service</h2>
<p>History (comma-separated): <input id="h" value="10,12,13,15,16,18" size="30"></p>
<p>Horizon: <input id="n" type="number" value="6" style="width:70px">
   Method: <select id="m"><option>trend</option><option>ma</option><option>naive</option></select>
   <button onclick="go()">Forecast</button></p>
<div id="out">result appears here</div>
<script>
async function go(){
  const history=document.getElementById('h').value.split(',').map(Number);
  const horizon=+document.getElementById('n').value, method=document.getElementById('m').value;
  const r=await fetch('/api/forecast',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({history,horizon,method})});
  document.getElementById('out').textContent=JSON.stringify(await r.json(),null,2);
}
</script>
</body></html>
"""
