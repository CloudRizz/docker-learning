```markdown
# 🐳 Flask Task Manager (Docker + Redis + Nginx)

A containerised full-stack **task manager application** built using Flask, Redis, Docker Compose, and Nginx reverse proxy. This project demonstrates a multi-tier architecture with persistence, container orchestration, and production-style deployment patterns.

---

## 🚀 Features

- 📝 Create, view, and delete tasks
- ⚡ REST API built with Flask
- 💾 Redis used for fast in-memory data storage with persistence
- 🌐 Nginx reverse proxy for routing traffic
- 🐳 Fully containerised using Docker Compose
- 🔁 Restart policies for reliability

---

## 🏗️ Architecture

```

Browser
↓
Nginx (Reverse Proxy)
↓
Flask App (Task API + UI)
↓
Redis (Data Store)

```

---

## 📦 Tech Stack

- Python (Flask)
- Redis
- Docker & Docker Compose
- Nginx
- HTML (basic UI)

---

## 📁 Project Structure

```

.
├── app.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
├── redis/
│   ├── Dockerfile
│   └── redis.conf
├── nginx/
│   └── nginx.conf
└── templates/
└── index.html

````

---

## ⚙️ How to Run Locally

### 1. Clone repository
```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
````

### 2. Build and start containers

```bash
docker-compose up --build
```

### 3. Open application

```
http://localhost:8080
```

---

## 🔌 API Endpoints

### ➕ Create task

```http
POST /api/tasks
```

### 📋 Get all tasks

```http
GET /api/tasks
```

### ❌ Delete task

```http
DELETE /api/tasks/<task_id>
```

---

## 🧪 Example Request

```bash
curl -X POST http://localhost:8080/api/tasks \
-H "Content-Type: application/json" \
-d '{"task":"Learn Docker"}'
```

---

## 🐳 Docker Services

| Service      | Description   |
| ------------ | ------------- |
| task-manager | Flask backend |
| redis        | Data storage  |
| nginx        | Reverse proxy |

---

## 🔁 CI/CD (GitHub Actions)

This project includes a basic CI pipeline that:

* Builds Docker images
* Validates docker-compose setup
* Spins up containers to verify system integrity

---

## 📈 Future Improvements

* JWT authentication
* React frontend
* AWS deployment (ECS/Fargate)
* Monitoring with Prometheus & Grafana
* WhatsApp bot integration

---

## 👨‍💻 Author

Built by Rizwan Hussain 

```
```
