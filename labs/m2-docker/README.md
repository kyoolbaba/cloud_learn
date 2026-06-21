---
tags: [lab, m2-docker]
aliases: [m2-docker lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# Module 2 — Docker (hands-on lab)

The highest-leverage skill in this whole plan. By the end you can package the
forecasting app + all its deps into one portable **image** that runs identically
on your laptop, a teammate's machine, or cloud hardware. That env-parity is what
makes the cloud step safe ("works on my laptop" → "works everywhere").

**Prereq:** Docker Desktop running (it's installed). In WSL/PowerShell:
```bash
docker version        # client AND server should both report versions
docker run hello-world
```
All commands below run from this folder: `labs/m2-docker/`.

---

## Core mental model

- **Image** = a frozen, read-only snapshot of an app + its dependencies (a class).
- **Container** = a running instance of an image (an object). Many containers from one image.
- **Layers** = each Dockerfile instruction is a cached layer; unchanged layers are reused → fast rebuilds.
- **Registry** = where images are stored/shared (Docker Hub now; AWS ECR in Module 4).

---

## Lab 1 — Run someone else's image

```bash
docker run -d -p 8080:80 --name web nginx   # -d detached, -p HOST:CONTAINER
curl localhost:8080                          # nginx's welcome page
docker ps                                    # running containers
docker logs web                              # its stdout
docker exec -it web bash                     # shell INTO the container; poke around, then: exit
docker stop web && docker rm web             # stop + remove
```
**Concept:** `-p 8080:80` maps your laptop's 8080 to the container's 80. Inside,
the app thinks it owns port 80; you reach it on 8080.

---

## Lab 2 — Build YOUR app image (the ready-made Dockerfile)

```bash
docker build -t forecast-app:0.1 .      # reads ./Dockerfile, tags the image
docker images | grep forecast-app       # see your image + its size
docker run --rm -p 8011:8011 forecast-app:0.1
#   open http://localhost:8011  -> the forecast UI. Try the form.
#   Ctrl-C to stop;  --rm auto-removes the container on exit.
```
Read the `Dockerfile` comments — especially **why requirements are copied and
installed before the app code** (layer caching).

---

## Lab 3 — Prove layer caching (the build-speed lesson)

```bash
# Edit sample_app/app.py (change the <h2> title), then rebuild:
docker build -t forecast-app:0.1 .
#   Watch the output: the pip-install layer says "CACHED" — only the COPY app +
#   below re-run. Editing code does NOT reinstall dependencies. That's the win.
```
Now break the cache on purpose: bump a version in `requirements.txt` and rebuild —
notice the install layer re-runs. Order in a Dockerfile = build speed.

---

## Lab 4 — Env vars and volumes (config + persistence)

```bash
# Inject config at run time with -e; mount a host folder with -v:
mkdir -p data
docker run --rm -p 8011:8011 \
  -e APP_ENV=prod -e APP_VERSION=9.9.9 \
  -v "$(pwd)/data:/data" \
  forecast-app:0.1
#   visit http://localhost:8011/api/info  -> shows env=prod, version 9.9.9,
#   data_dir_mounted=true. The container is stateless; the VOLUME keeps data.
```
**Concept:** containers are disposable. Anything you must keep (your `pudbo_store`
projects) lives in a **volume** mounted from outside, so it survives `docker rm`.

---

## Lab 5 — .dockerignore (smaller, faster builds)

The ready-made `.dockerignore` already excludes `.venv/`, caches, `*.parquet`,
`frozen/`, `pudbo_store/`. To feel the difference, temporarily rename it and
rebuild — the "transferring context" size jumps. Then restore it.

---

## Lab 6 — docker compose (declare it instead of typing flags)

```bash
docker compose up --build        # builds + runs per docker-compose.yml; Ctrl-C stops
#   same app, but ports/env/volumes/healthcheck are declared in one file.
docker compose up -d             # background
docker compose ps                # status (note 'healthy' from the healthcheck)
docker compose logs -f           # follow logs
docker compose down              # stop + remove everything
```
This is how multi-container apps (app + db + cache) are wired and started together.

---

## Lab 7 — Push to a registry (Docker Hub now, ECR in M4)

```bash
docker login                                          # free Docker Hub account
docker tag forecast-app:0.1 <your-dockerhub-user>/forecast-app:0.1
docker push <your-dockerhub-user>/forecast-app:0.1
#   now anyone (incl. a cloud machine) can `docker pull` and run the exact image.
```
In Module 4 you'll push this same image to **AWS ECR** instead and run it on
**Fargate** — no servers to manage.

---

## Cleanup (reclaim disk)

```bash
docker ps -a                # all containers, incl. stopped
docker container prune      # remove stopped containers
docker image prune          # remove dangling images
docker system df            # how much disk Docker is using
```

---

**Checkpoint (M2 done):** you can write a Dockerfile from scratch, build & run the
app with the port mapped and data persisted in a volume, explain image-vs-container
and layer caching, and push to a registry. Tick the **Docker** boxes in
`../../PROGRESS.md`.

**Swap in your real app later:** drop `db_polars_app.py` (and friends) into
`sample_app/`, add the heavy deps to `requirements.txt`, point `CMD` at
`db_polars_app:app`. Everything else stays the same. → Then **Module 3 — AWS core.**
