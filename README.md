# Yoo REST API

A beginner FastAPI project implementing full CRUD operations on an in-memory user store.

---

## Requirements

- Python 3.10+
- fastapi
- uvicorn

---

## Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# Install dependencies
pip install fastapi uvicorn
```

---

## Run

```bash
fastapi run main.py          # production
uvicorn main:app --reload    # development (auto-restarts on file save)
```

Server starts at: `http://0.0.0.0:8000`

---

## Interactive Docs

| UI       | URL                              |
|----------|----------------------------------|
| Swagger  | http://127.0.0.1:8000/docs       |
| ReDoc    | http://127.0.0.1:8000/redoc      |

---

## API Endpoints

| Method   | Endpoint            | Description         | Status Code |
|----------|---------------------|---------------------|-------------|
| GET      | `/`                 | Health check        | 200         |
| GET      | `/users`            | List all users      | 200         |
| GET      | `/users/{user_id}`  | Get user by ID      | 200         |
| POST     | `/users`            | Create a new user   | 201         |
| PATCH    | `/users/{user_id}`  | Partially update    | 200         |
| DELETE   | `/users/{user_id}`  | Delete a user       | 200         |

---

## Request & Response Examples

### POST `/users`
**Request body:**
```json
{
  "name": "Lochan",
  "age": 21
}
```
**Response:**
```json
{
  "id": 6,
  "name": "Lochan",
  "age": 21
}
```

### PATCH `/users/6`
**Request body (partial — send only what you want to change):**
```json
{
  "age": 22
}
```
**Response:**
```json
{
  "id": 6,
  "name": "Lochan",
  "age": 22
}
```

### DELETE `/users/6`
**Response:**
```json
{
  "message": "User 6 deleted"
}
```

---

## Data Models

### UserCreate
| Field | Type | Required |
|-------|------|----------|
| name  | str  | Yes      |
| age   | int  | Yes      |

### UserUpdate
| Field | Type | Required |
|-------|------|----------|
| name  | str  | No       |
| age   | int  | No       |

### UserResponse
| Field | Type | Description       |
|-------|------|-------------------|
| id    | int  | Auto-assigned ID  |
| name  | str  | User's name       |
| age   | int  | User's age        |

---

## Error Responses

| Status Code | Reason                        |
|-------------|-------------------------------|
| 404         | User not found                |
| 422         | Invalid request body/params   |

---

## Notes

- Data is stored **in-memory** — all changes reset when the server restarts.
- No authentication, no database. This is intentional for learning purposes.
- Next steps: swap `fake_db` for SQLite via SQLAlchemy, add `Field` validators, add `Depends()` for auth.
