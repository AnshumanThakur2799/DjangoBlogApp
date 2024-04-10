# Simple Blog Application

This is a simple Django application for managing blog posts and comments.

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/AnshumanThakur2799/DjangoBlogApp.git
```
2. Create a virtual environment:
```bash
python -m venv venv
``` 
3. Activate the virtual environment:

- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Navigate to the project directory:
```bash
cd blog
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Apply migrations:
```bash
python mange.py makemigrations
```
```bash
python manage.py migrate
```

7. Create a superuser to access the Django admin panel:
```bash
python manage.py createsuperuser
```
8. Start the development server:
```bash
python manage.py runserver
```

The application will be accessible at `http://localhost:8000/`.

## API Endpoints

## Blogs

### 1. List Posts

- **Endpoint:** `/posts/`
- **Method:** GET
- **Description:** Retrieves a list of all posts with pagination.
- **Parameters:**
  - `page`: Page number (default: 1)
  - `page_size`: Number of posts per page (default: 10)
- **Example Response:**

```json
{
  "results": [
    {
      "id": 1,
      "title": "Example Post 1",
      "content": "Lorem ipsum dolor sit amet...",
      "author": "user@example.com",
      "published_date": "2024-04-10T12:00:00Z",
      "comments": []
    },
    {
      "id": 2,
      "title": "Example Post 2",
      "content": "Lorem ipsum dolor sit amet...",
      "author": "user@example.com",
      "published_date": "2024-04-10T12:00:00Z",
      "comments": []
    }
  ],
  "total_pages": 2,
  "current_page": 1
}
```
### 2. Create Post

- **Endpoint:** `/posts/create`
- **Method:** POST
- **Description:** create a new post
- **Parameters:**
  - `title`: title of post
  - `content`: content of post
- **Example Response:**
```json
{
  "title": "New Post",
  "content": "This is the content of the new post."
}
```

### 3. Retrieve, Update, and Delete Post
- **Endpoint:** `/posts/<int:pk>/`
- **Method:** GET (retrieve) / PUT (update) / DELETE
- **Description:** Retrieve, update, or delete a specific post by ID.
- **Parameters:**
  - `title`: title of post
  - `content`: content of post

- **Example Request (PUT):**
  ```json
  {
  "title": "Updated Post Title",
  "content": "Updated content of the post."
  }
  ```
  - **Example Request (GET):**
  ```json
  {
  "id": 1,
  "title": "Updated Post Title",
  "content": "Updated content of the post.",
  "author": "user@example.com",
  "published_date": "2024-04-10T12:00:00Z",
  "comments": []
  }
  ```
 
  
### 4. Add Comment to Post

- **Endpoint:** `/posts/<int:post_id>/comments/`
- **Method:** POST
- **Description:** create a new post
- **Parameters:**
  - `title`: title of post
  - `content`: Adds a new comment to a specific post.
- **Request Payload:**
```json
{
  "text": "Comment text",
  "author": "<user_id>"
}

```
### 5. Edit or Delete Comment

- **Endpoint:** `/posts/<int:post_id>/comments/<int:comment_id>/`
- **Method:** PUT or DELETE
- **Description:** Edit or delete a specific comment on a post.
- **Parameters:**
  - `title`: title of post
  - `content`: Adds a new comment to a specific post.
- **Example Request (PUT):**
```json
{
  "text": "Edited comment text."
}
```
- **Example Request (DELETE):**
```json
{
  "message": "Comment deleted successfully"
}

```

## Users

### 6. Register User

- **Endpoint:** `users/registration/`
- **Method:** POST
- **Description:**  Registers a new user
- **Parameters:**
  - `username`: username of user
  - `password`: password of the user
- **Example Request:**
```json
{
  "username": "new_user",
  "password": "password123",
  "email": "new_user@example.com"
}

```
- **Example Response:**
```json
{
  "status": 200,
  "payload": {
    "username": "new_user",
    "email": "new_user@example.com"
  },
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "message": "User registered successfully"
}
```
