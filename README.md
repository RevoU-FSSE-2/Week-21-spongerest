# Twitter BackEnd App Using Python Flask

## Installation

To set up the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/RevoU-FSSE-2/Week-21-spongerest.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Week-21-spongerest
    ```

3. Install dependencies using Pipenv:

    ```bash
    pipenv install
    ```

    This will install the required packages specified in the Pipfile.

4. Activate the virtual environment:

    ```bash
    pipenv shell
    ```

## Configuration

1. Create a `.env` file in the project root and configure environment variables:

    ```env
    DATABASE_URL = "postgresql://postgres:kehidupan#######@db.vsctwhcxyylhgovydcew.supabase.co:5432/postgres"
    SECRET_KEY = "4hy4n6#######"
    ```

## Usage

Run the Flask application:

```bash
flask run
```

# Database Setup for Flask Application

This module (`db.py`) contains the configuration for Flask application's database using Flask-SQLAlchemy.

## Installation

To set up the database, make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install Flask-SQLAlchemy
```

# Usage
## Access different parts of application using the registered blueprints:

1. Auth: http://localhost:5000/auth/
2. User: http://localhost:5000/user/
3. Tweet: http://localhost:5000/tweet/
4. Following: http://localhost:5000/following/

## https://www.postman.com/joint-operations-administrator-82737956/workspace/revou/collection/28997654-dd0f00d6-6a9a-4e03-85a9-c37874d83db1

# User API

This module (`user.py`) defines the User API for Flask application. It includes functionality to retrieve user profiles and related information.

## Usage

### Get User Profile

**Endpoint:** `GET /user/`

**Description:** Retrieve the profile information for the authenticated user.

**Request:**
- Headers:
  - `Authorization`: Bearer token for authentication.

**Response:**
- Success (200 OK):
  ```json
  {
    "id": 1,
    "username": "example_user",
    "bio": "A brief user bio.",
    "followers": 10,
    "following": 20,
    "tweet": [
      {
        "id": 1,
        "tweet": "Example tweet content.",
        "publish_at": "2023-11-25T12:00:00Z"
      },
      // Additional tweet objects...
    ]
  }
  ``````

# User Model

This module (`model.py`) defines the User model for  Flask application. It represents the structure of the `user` table in the database.

## Fields

- `id`: Integer, Primary Key.
- `username`: String(20), Unique, Not Null. The username of the user.
- `password`: String(100), Not Null. The hashed password of the user.
- `bio`: String(200), Not Null. A brief biography or description of the user.
- `followers`: Integer, Default: 0. The count of followers for the user.
- `following`: Integer, Default: 0. The count of users that the user is following.

## Relationships

- `following_relations`: One-to-Many relationship with the `Following` model. Represents the users followed by the current user.


## Dependencies
1. Flask: Web framework for building the application.
2. Flask-SQLAlchemy: SQL Alchemy integration with Flask.
3. Psycopg2-binary: PostgreSQL adapter for Python.
4. Bcrypt: Password hashing library.
5. Flask-Bcrypt: Bcrypt extension for Flask.
6. Marshmallow: Object serialization/deserialization library.
7. Injector: Dependency injection framework.
8. PyJWT: JSON Web Token implementation for Python.
9. Python-Dotenv: Load environment variables from a .env file.



## Requirements
1. Python 3.12

## License
This project is licensed under the MIT License.
