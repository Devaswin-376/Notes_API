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
```

---

## Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Devaswin-376/Notes_API.git
cd Notes_API
```
### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set environment variables
```bash
Create .env file (do not commit it).
```
### 5. Run migrations
```bash
alembic upgrade head
```
### 6. Start the server
```bash
uvicorn app.main:app --reload
```
### API will be available at:
http://127.0.0.1:8000/docs↗️
    
### Running Tests
```bash
pytest
```
---

## Postman Collection
A Postman collection with:
- Example requests
+ JWT auth flow
* Basic tests
Included in repository 📁:
```pgsql
postman/Auth_API.postman_collection.json
postman/Notes_API.postman_collection.json
```
---

## Deployment🚀:
The application is deployed on Render using:
+ Python Web Service
* Build command:
```bash
pip install -r requirements.txt
```
* Start command:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```
---

### 👤 Author
  
Devaswin K.S<br>
Diploma in Computer Engineering  
Backend Developer (FastAPI, PostgreSQL)  

---

### 📄 License
This project is created for educational and evaluation purposes.
