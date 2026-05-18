# Flask Redis Docker Application

A multi-container application built with Flask, Redis, Docker and Docker Compose.

This project demonstrates how to containerize multiple services, enable inter-container communication, persist Redis data using Docker volumes, and manage the entire application stack with Docker Compose.

---

# Project Overview

The application consists of:

- A Python Flask web application
- A Redis database
- Docker containers for both services
- Docker Compose orchestration

The Flask application connects to Redis to store and retrieve a visit counter.

---

# Architecture

```text
Browser
   │
   ▼
Flask Container
   │
   ▼
Redis Container
   │
   ▼
Docker Volume
```

---

# Features

- Multi-container Docker application
- Flask web application with two routes
- Redis key-value datastore integration
- Docker Compose orchestration
- Environment variable configuration
- Persistent Redis storage using Docker volumes
- Custom Dockerfiles for both Flask and Redis

---

# Application Routes

| Route | Description |
|---|---|
| `/` | Displays a welcome message |
| `/count` | Increments and displays the visitor count stored in Redis |

---

# Technologies Used

- Python
- Flask
- Redis
- Docker
- Docker Compose

---

# Project Structure

```bash
multi-container-visitor-app/
│
├── .gitignore
├── docker-compose.yml
│
├── flask-app/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── redis/
│   ├── Dockerfile
│   └── redis.conf
│
└── README.md
```

---

# How to Run the Project

## Clone the Repository

```bash
git clone git@github.com:CloudRizz/flask-redis-docker-app.git
cd flask-redis-docker-app
```

---

## Build and Start Containers

```bash
docker compose up --build
```

---

# Access the Application

## Welcome Page

Open:

```text
http://localhost:5000
```

Example response:

```text
Hello from Rizwan Hussain!!!
```

---

## Visitor Counter

Open:

```text
http://localhost:5000/count
```

Refresh the page multiple times to see the count increment.

Example:

```text
Visitor count: 1
Visitor count: 2
Visitor count: 3
```

---

# Persistent Storage

Redis data is persisted using Docker volumes.

This ensures the visitor count remains available even after containers are stopped and restarted.

---

# Environment Variables

The Flask application reads Redis connection details from environment variables configured in `docker-compose.yml`.

Example:

```yaml
environment:
  REDIS_HOST: redis
  REDIS_PORT: 6379
```

---

# Docker Compose Services

## Flask Service

- Builds custom Flask Docker image
- Exposes port `5000`
- Connects to Redis service

## Redis Service

- Builds custom Redis Docker image
- Uses persistent Docker volume
- Stores visitor count data

---

# Learning Outcomes

This project helped demonstrate:

- Containerization with Docker
- Multi-container applications
- Docker Compose orchestration
- Service-to-service communication
- Persistent storage with Docker volumes
- Environment variable management
- Redis integration with Flask

---

# Future Improvements

Potential future enhancements:

- Add Nginx reverse proxy
- Implement Gunicorn for production deployments
- Add health checks
- Add CI/CD pipeline with GitHub Actions
- Deploy to AWS ECS or Kubernetes
- Add application monitoring and logging

---

# Author

Rizwan Hussain

Cloud Engineer | AWS | DevOps | Docker | Terraform | CI/CD