# Car Dealership Project

This is a Django project for a car dealership website. It provides a platform for managing car listings, customer inquiries, and sales.

## Project Structure

```
car_dealership/
├── car_dealership/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dealership/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd car_dealership
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```
   python manage.py migrate
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Access the website at `http://127.0.0.1:8000/`.
- Use the Django admin interface to manage car listings and customer inquiries.

## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.