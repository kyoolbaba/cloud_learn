# Dockerfile — package the sample forecast app into a portable image.
# Build:  docker build -t forecast-app:0.1 .
# Run:    docker run --rm -p 8011:8011 forecast-app:0.1   -> http://localhost:8011
#
# Each instruction is a cached LAYER. Order matters: things that change rarely
# (deps) go ABOVE things that change often (your code), so editing app.py doesn't
# re-install dependencies. That's the #1 Docker build-speed lesson.

FROM python:3.12-slim                 # small official Python base image

# Good-practice env: no .pyc files, unbuffered logs (so you see prints live)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app                          # all following paths are relative to /app

# 1) Copy ONLY requirements first and install — this layer is cached and reused
#    on every rebuild as long as requirements.txt doesn't change.
COPY sample_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Now copy the app code. Editing app.py invalidates only from here down,
#    so rebuilds are near-instant (deps layer stays cached).
COPY sample_app/ .

EXPOSE 8011                           # documents the port (doesn't publish it; -p does)

# A healthcheck Docker can use to know the container is actually serving
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8011/health').status==200 else 1)"

# Start the server, bound to 0.0.0.0 so it's reachable from outside the container
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8011"]
