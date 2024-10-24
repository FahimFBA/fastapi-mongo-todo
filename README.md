# To-Do Backend API with FastAPI and MongoDB

This is a simple **To-Do backend** built with **FastAPI** and **MongoDB**. The API allows users to manage their to-do tasks through standard REST operations. It uses **MongoDB** as the database and **Pydantic** for request validation.

## Project Structure

```bash
├── config/           # Contains configuration-related files (e.g., database connection)
├── models/           # Defines MongoDB models
├── routes/           # Contains route definitions (e.g., CRUD operations)
├── schema/           # Defines the Pydantic models for request/response validation
├── main.py           # The main entry point for the FastAPI app
├── .env.example      # Environment variables example (MongoDB credentials)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## Features

- **Create, Read, Update, Delete (CRUD)** to-do tasks.
- **FastAPI** for fast, modern, and asynchronous Python API development.
- **MongoDB** as the NoSQL database.
- **Pydantic** for data validation.
- Supports environment variables via `.env` for MongoDB credentials.

## Requirements

- **Python 3.9+**
- **MongoDB Atlas** (or local MongoDB instance)
- **FastAPI**
- **Uvicorn**
- **Pymongo**
- **Pydantic**
- **dotenv** for environment variables

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/FahimFBA/fastapi-mongo-todo.git
   cd fastapi-mongo-todo
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root and add your MongoDB credentials:**

   **.env**
   ```env
    MONGO_USERNAME=
    MONGO_PASSWORD=
   ```

## Configuration

The **config** directory contains the configuration for connecting to MongoDB. The database connection string is dynamically created using the environment variables.

```python
# config/database.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the MongoDB credentials from the environment variables
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER_URL")

# Create the MongoDB connection URI using the loaded credentials
uri = f"mongodb+srv://{username}:{password}@{
    cluster}/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize MongoDB client and access the database and collection
client = MongoClient(uri)
db = client.todo_db
collection_name = db["todo_collection"]
```

## Running the Application

1. **Start the FastAPI server:**

   You can run the FastAPI application using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   or,

   ```bash
   fastapi dev main.py
   ```

   The app will run on `http://127.0.0.1:8000`.

2. **API Documentation:**

   FastAPI automatically generates interactive API docs:
   - **Swagger UI:** Visit `http://127.0.0.1:8000/docs`
   - **Redoc UI:** Visit `http://127.0.0.1:8000/redoc`

## API Endpoints

### Base URL: `/todos`

| Method | Endpoint       | Description              |
|--------|----------------|--------------------------|
| GET    | `/`            | Get all to-do items       |
| POST   | `/`            | Create a new to-do        |
| PUT    | `/{id}`        | Update a to-do by ID      |
| DELETE | `/{id}`        | Delete a to-do by ID      |

### Code Breakdown:
- **GET `/todos/`**: Fetch all to-do items from the database.
- **POST `/todos/`**: Create a new to-do item in the database.
- **PUT `/todos/{id}`**: Update an existing to-do by its MongoDB object ID.
- **DELETE `/todos/{id}`**: Delete an existing to-do by its MongoDB object ID.


### Example To-Do Item Schema

```json
{
  "title": "Finish project",
  "description": "Work on the FastAPI backend",
  "completed": false
}
```

## Project Structure

### `/config`
Contains configuration files, including the MongoDB connection setup.

### `/models`
Defines the MongoDB data models. This is where the schema for your MongoDB collections resides.

### `/routes`
Contains the route definitions for handling HTTP requests such as creating, reading, updating, and deleting tasks.

Example route for deleting a to-do:

```python
# routes/todo.py

from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# DELETE Request Method
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

```

### `/schema`
Defines the Pydantic models for data validation and serialization of requests and responses.

```python
# schema/schemas.py

def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]
```

## Deployment

You can deploy this FastAPI app to platforms like:

- **Deta**
- **Render**
- **Railway**
- **Fly.io**

You can also use **MongoDB Atlas** as a managed cloud MongoDB instance.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the [MIT](./LICENSE) License.
