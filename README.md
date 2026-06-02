# PrimeTrade Task Management API

A robust, full-stack task management system built with FastAPI and PostgreSQL. This application features secure JWT-based authentication, Role-Based Access Control (RBAC), and a fully containerized deployment environment using Docker.

## 🚀 Features

* **Secure Authentication:** JWT (JSON Web Token) implementation for secure login and session management.
* **Role-Based Access Control (RBAC):** Distinct capability tiers for standard `user` and `admin` roles, ensuring strict data privacy and system security.
* **Full CRUD Functionality:** Create, Read, Update, and Delete operations for task management.
* **Relational Database:** Migrated from SQLite to an enterprise-grade PostgreSQL database.
* **Containerized Deployment:** Fully reproducible development and production environments using Docker and Docker Compose.
* **Interactive Frontend:** A vanilla JavaScript and HTML dashboard demonstrating seamless API integration and dynamic DOM rendering.

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI (Python 3.10+)
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** Passlib (Bcrypt), python-jose (JWT)
* **Containerization:** Docker & Docker Compose
* **Frontend:** HTML, CSS, Vanilla JavaScript

## 📦 Getting Started

### Prerequisites
* Docker and Docker Compose installed on your machine.
* Git

### Installation & Execution (Docker - Recommended)

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
