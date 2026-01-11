# Notes API

A secure RESTful Notes API built with FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication.  
Supports note versioning, restoration, and full CRUD operations.

---

## Features

- User registration & login (JWT authentication)
- Create, update, and manage notes
- Automatic note versioning
- View version history
- Restore previous versions
- PostgreSQL as primary database
- Pytest-based automated testing
- Postman API tests
- Deployed on Render

---

## Tech Stack

- FastAPI
- PostgreSQL (Neon)
- SQLAlchemy ORM
- Alembic Migrations
- JWT Authentication
- Pytest
- Postman
- Render (Deployment)

---

## Environment Variables

```env
DATABASE_URL=postgresql://<username>:<password>@<host>/<db>?sslmode=require
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

## Running Locally

1. Clone the repository
    git clone https://github.com/Devaswin-376/Notes_API.git
    cd Notes_API

