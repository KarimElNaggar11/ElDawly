# El Dawly Real Estate

A professional real estate website for El Dawly, showcasing over 300 apartments in Vienna, Austria.

## Features

- Property listings with detailed information
- Advanced search and filtering
- Property image galleries
- Contact forms
- Admin dashboard
- Responsive design

## Tech Stack

- Backend: Django (Python)
- Database: SQLite
- Frontend: HTML, CSS (Bootstrap), JavaScript
- External Libraries: 
  - Django REST Framework
  - Bootstrap
  - pytest

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
eldawly/
├── manage.py
├── requirements.txt
├── eldawly/          # Main project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── properties/       # Properties app
├── accounts/        # User accounts app
├── static/          # Static files
└── templates/       # HTML templates
```

## Contributing

Please read our contributing guidelines before submitting pull requests.

## License

This project is proprietary and confidential. 