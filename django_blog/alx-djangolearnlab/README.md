# django_blog Project

This is a Django project named `django_blog` which includes a blog application for managing posts.

## Project Structure

```
alx-djangolearnlab
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── django_blog
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Features

- **Post Model**: The blog app includes a `Post` model with the following fields:
  - `title`: A character field with a maximum length of 200 characters.
  - `content`: A text field for the post content.
  - `published_date`: A date-time field that automatically sets the date when the post is created.
  - `author`: A foreign key relation to Django’s User model, allowing multiple posts by a single author.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/alx-djangolearnlab.git
   ```

2. Navigate into the project directory:
   ```
   cd alx-djangolearnlab
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```
   python manage.py makemigrations blog
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

You can access the blog application at `http://127.0.0.1:8000/`. 

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.