# AI Backend Deployment Project

## Project Overview

This project demonstrates how to deploy and productionize a backend application using:

- FastAPI
- PostgreSQL
- Redis
- NGINX Reverse Proxy
- Docker & Docker Compose
- GitHub Actions CI/CD
- Ubuntu VPS Server

The goal of this assignment is to showcase production deployment practices, infrastructure organization, security awareness, and CI/CD automation.

---

# Architecture

Client Request
       |
    NGINX
       |
   FastAPI App
    |       |     
PostgreSQL Redis

---

# Tech Stack

| Component | Technology |
|----------|-------------|
| Backend API | FastAPI |
| Database | PostgreSQL |
| Cache/Broker | Redis |
| Reverse Proxy | NGINX |
| Containerization | Docker |
| Orchestration | Docker Compose |
| CI/CD | GitHub Actions |
| Hosting | Ubuntu VPS |

---

# Features

- Dockerized FastAPI application
- PostgreSQL database integration
- Redis integration
- NGINX reverse proxy setup
- Health check endpoint
- GitHub Actions automated deployment
- Environment variable configuration
- Restart policies
- Logging strategy
- Backup strategy documentation
- Basic production security measures

---

# Project Structure

```bash
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docker-compose.yml
├── .env
└── README.md
