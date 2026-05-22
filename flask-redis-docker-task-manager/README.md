````markdown
# 🐳 Flask Redis Task Manager (Docker + CI/CD)

A containerised full-stack task manager application built using **Flask, Redis, and Docker Compose**, with a complete **CI/CD pipeline using GitHub Actions**.

This project demonstrates a production-style multi-container architecture with background task processing, reverse proxying, and automated deployment workflows.

---

## 🚀 Features

- 📝 Create and manage tasks via a Flask web UI
- ⚡ Asynchronous background task processing using Redis queue
- 🔁 Worker-based architecture for handling long-running jobs
- 🐳 Fully containerised with Docker & Docker Compose
- 🌐 Nginx reverse proxy for routing traffic (if enabled in setup)
- 🚀 CI/CD pipeline using GitHub Actions
- ✅ Automated build + validation workflow on every push

---

## 🏗️ Architecture

The system is split into multiple services:

- **Flask Web App (Server)**  
  Handles HTTP requests, UI rendering, and task creation

- **Redis (Message Broker / Queue)**  
  Stores task queue and job state for asynchronous processing

- **Worker Service**  
  Consumes tasks from Redis and processes them in the background

- **Nginx (Optional Reverse Proxy)**  
  Routes external traffic to the Flask application for production-style deployment

All services communicate over a Docker Compose network.

---

## ⚙️ Tech Stack

- Python (Flask)
- Redis
- Docker & Docker Compose
- Nginx
- GitHub Actions (CI/CD)

---

## 🔄 CI/CD Pipeline

This project includes a GitHub Actions workflow that automates build and validation.

### Pipeline Flow (on push to `main`):

1. Checkout repository
2. Build Docker images (Flask + Worker + Nginx if applicable)
3. Validate container builds
4. Run optional tests (if configured)
5. Prepare for deployment stage (future enhancement)

### Benefits

- Ensures consistent builds across environments
- Prevents broken code from being containerised
- Automates manual Docker build steps
- Sets foundation for full deployment automation

---

## 🐳 Running Locally

```bash
git clone https://github.com/CloudRizz/docker-learning.git
cd flask-redis-docker-task-manager

docker compose up --build
````

Once running, access the app:

```
http://localhost:5000
```

> If Nginx is enabled, the app may be accessible via `http://localhost` (port 80)

---

## 🔧 Key Improvements

* Introduced **CI/CD automation via GitHub Actions**
* Improved separation of concerns (web / worker / broker)
* Containerised full system using Docker Compose
* Added production-style reverse proxy pattern (Nginx)
* Standardised service communication via Redis queue

---

## 📌 Future Improvements

* Add unit + integration tests in CI pipeline
* Add security scanning (Trivy / Snyk)
* Deploy via AWS (ECS / EC2) using CD pipeline
* Add observability (Prometheus + Grafana)
* Migrate to Kubernetes for advanced orchestration practice

---

## 🧠 What this project demonstrates

* Microservices-style architecture design
* Asynchronous task processing
* Docker-based container orchestration
* CI/CD automation with GitHub Actions
* Production-minded DevOps thinking

---
