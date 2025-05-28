# 🧮 Flask Arithmetic Microservices + Template App

This project demonstrates a microservice architecture using Flask and Docker Compose. Each arithmetic operation (`+`, `-`, `*`, `/`) is implemented as a separate Flask API running in its own container. A front-end Flask application (template app) provides a user interface to interact with all the APIs.

---

## 📁 Project Structure

├── cliente/ # Frontend Flask app
│ ├── cliente.py
│ ├── templates/
│ │ └── show_all.html
│ │── Dockerfile
│ └── requirements.txt
├── app/ #main api
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── suma/
│ ├── app.py
│ │── Dockerfile
│ └── requirements.txt
├── resta/
│ ├── app.py
│ │── Dockerfile
│ └── requirements.txt
├── multiplicacion/
│ ├── app.py
│ │── Dockerfile
│ └── requirements.txt
├── division/
│ ├── app.py
│ │── Dockerfile
│ └── requirements.txt
└── docker-compose.yml

---

## 🚀 Getting Started

### 1. Install Docker and Docker Compose

Make sure you have Docker and Docker Compose installed on your system.

- [Docker Desktop (Windows/macOS)](https://www.docker.com/products/docker-desktop)
- `sudo apt install docker docker-compose` (Linux)

---

### 2. Run All Services

```bash
docker-compose up --build

