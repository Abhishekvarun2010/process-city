# Process City

Dockerized environment for Python development, system inspection, and stress testing (`htop`, `procps`, `stress-ng`).

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) & Docker Compose installed and running.

---

## Steps to Run

### 1. Build and Start the Container
Start the container in detached mode:
```bash
docker compose up -d --build
```

### 2. Access the Interactive Shell
Open a bash session inside the container:
```bash
docker compose exec process-city bash
```

### 3. Verify Installed Tools
Inside the container, verify the environment and tools:
```bash
python3 --version
htop
stress-ng --version
```

### 4. View Container Logs
Check logs if needed:
```bash
docker compose logs -f process-city
```

### 5. Stop the Container
To stop and remove the container:
```bash
docker compose down
```
