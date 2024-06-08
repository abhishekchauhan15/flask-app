# Flask MongoDB ToDo App

This is a simple ToDo application built with Flask as the backend framework and MongoDB as the database. The application supports JWT token validation for user authentication and includes basic CRUD operations for managing ToDo items.

## Features

- User authentication with JWT
- Create, read, update, and delete ToDo items
- JWT token validation middleware

## Technologies Used

- Flask
- MongoDB
- PyMongo
- Flask-JWT-Extended
- Docker

## Setup Instructions

### Prerequisites

- Python 3.9 or later
- Docker

### Local Setup without Docker

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd flask_mongo_todo
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure environment variables in `config.py`:**
    ```python
    import os

    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
        MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://flask-app:flask@flask.xv7avzt.mongodb.net/?retryWrites=true&w=majority&appName=flask'
    ```

6. **Run the application:**
    ```bash
    flask run
    ```

7. **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

### Setup with Docker

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd flask_mongo_todo
    ```

2. **Build the Docker image:**
    ```bash
    docker build -t flask-mongo-todo .
    ```

3. **Run the Docker container, passing environment variables:**
    ```bash
    docker run -e SECRET_KEY=your_secret_key -e MONGO_URI='mongodb+srv://flask-app:flask@flask.xv7avzt.mongodb.net/?retryWrites=true&w=majority&appName=flask' -p 5000:5000 flask-mongo-todo
    ```

4. **Access the application:**
    Open your web browser and go to `http://localhost:5000`.
