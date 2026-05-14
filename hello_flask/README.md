```md
# Flask + MySQL Docker Practice Project

This is a small practice project built to understand how to containerise a Python Flask application 
and connect it to a MySQL database using Docker and Docker Compose.

The goal of this project was to learn:
- How to build a multi-container application
- How to connect services using Docker networking
- How to use Docker Compose to orchestrate services
- How to use a multi-stage Docker build for a Python app
- How Flask connects to a MySQL database using `mysqlclient`

---

## 📦 Tech Stack

- Python 3.8
- Flask
- MySQL 8
- Docker
- Docker Compose
- MySQLClient (Python driver)

---

## 🏗️ Architecture Overview

The project contains two services:

### 1. Web (Flask App)
- Built using a multi-stage Dockerfile
- Runs a simple Flask web server
- Connects to the MySQL container on startup
- Queries the database for the MySQL version

### 2. Database (MySQL)
- Official MySQL 8 image
- Runs as a separate container
- Exposed internally to the Flask app via Docker networking

---

## 📁 Project Structure

```

.
├── app.py
├── Dockerfile
├── docker-compose.yml
└── README.md

```

---

## 🚀 How It Works

When you access the Flask app in the browser:

1. Flask starts and listens on port `5000`
2. It connects to the MySQL container (`mydb`)
3. Executes the query:
   ```sql
   SELECT VERSION();
````

4. Returns the MySQL version in the browser

Example output:

```
Hello, World! MySQL version: 8.0.xx
```

---

## 🐳 Running the Project

### 1. Build and start containers

```bash
docker-compose up --build
```

### 2. Open in browser

```
http://localhost:5000
```

---

## 🔌 Docker Networking

Docker Compose automatically creates a network, allowing containers to communicate using service names:

* `web` → Flask application
* `mydb` → MySQL database hostname used inside the app

Example:

```
# python
host="mydb"
```

---

## 🧠 Key Learnings

### ✔ Flask + Database Integration

* How to connect a Python app to MySQL using `mysqlclient`

### ✔ Docker Compose

* Multi-container orchestration
* Service dependencies using `depends_on`

### ✔ Multi-stage Docker Build

* Build dependencies separated from runtime image
* Smaller and cleaner production image

---

## ⚠️ Notes

* This is a **development/demo project**, not production-ready
* Passwords are hardcoded for simplicity
* No persistent volume is configured for MySQL data
* No health checks or retry logic implemented

---

## 📌 Possible Improvements

* Add MySQL persistent volume
* Add environment variable support (`.env`)
* Add health checks for database readiness
* Use production WSGI server (e.g. Gunicorn)
* Improve security (no hardcoded credentials)

---

## 🐳 Practice project for learning Docker, Flask, and MySQL integration.
