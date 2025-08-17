# django_blog Project

This project is a simple Django blog application that allows users to create and manage blog posts.

## Project Structure

```
django_blog/
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── django_blog/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Features

- Create, read, update, and delete blog posts.
- Each post has a title, content, published date, and an author.
- Admin interface for managing posts.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd django_blog
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the blog at `http://127.0.0.1:8000/`.
- Use the Django admin interface to manage posts at `http://127.0.0.1:8000/admin/`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.