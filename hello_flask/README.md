
# 🐳 Flask + MySQL Docker Practice Project

> A containerised Flask application connected to a MySQL database using Docker Compose and a multi-stage Docker build.

---

## ⚡ What This Project Demonstrates

- Multi-container Docker architecture
- Flask ↔ MySQL networking
- Docker Compose orchestration
- Multi-stage Docker builds
- Basic database connectivity from Python

---

## 🧱 Tech Stack

🐍 Python (Flask)  
🐬 MySQL 8  
🐳 Docker  
📦 Docker Compose  
🔌 mysqlclient

---

## 🏗️ Architecture

```

Browser → Flask App (Container) → MySQL DB (Container)

```

- Flask runs on port `5000`
- MySQL runs internally on Docker network (`mydb`)
- Flask queries DB version on request

---

## 📁 Project Structure

```

.
├── app.py
├── Dockerfile
├── docker-compose.yml
└── README.md

````

---

## 🚀 How to Run

```bash
docker-compose up --build
````

Then open:

```
http://localhost:5000
```

---

## 🔍 What Happens

1. Flask starts inside container
2. Connects to MySQL container (`mydb`)
3. Runs:

```sql
SELECT VERSION();
```

4. Returns result in browser

---

## 🐳 Docker Concepts Used

### 🔹 Docker Compose

Used to manage multiple containers together

### 🔹 Service Networking

Containers communicate using service names:

* `mydb` (not localhost)

### 🔹 Multi-stage Build

Reduces image size by separating build + runtime

---

## ⚠️ Limitations

* Hardcoded credentials (dev only)
* No persistent database storage
* No health checks
* Uses Flask dev server (not production-ready)

---

## 📌 Improvements (Next Steps)

* Add `.env` file for secrets
* Add MySQL volume for persistence
* Replace Flask dev server with Gunicorn
* Add health checks
* Add CI/CD pipeline (GitHub Actions)

---

## 👨‍💻 Author

Built for learning Docker, Flask, and container networking.

