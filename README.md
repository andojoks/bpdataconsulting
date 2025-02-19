# bpdata Consulting

Welcome to the bpdata Consulting website project. This application is built on the Django framework using Python 3.13 and serves as the foundational platform for bpdata Consulting’s online presence. The project is designed to efficiently support both development and production environments.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Development](#development)
- [Production](#production)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Responsive Design:** Mobile-first approach ensuring usability across devices.
- **Admin Interface:** Robust Django admin for managing content and user data.
- **Authentication:** Secure user registration, login, and profile management.
- **Consulting Services:** Detailed pages and features highlighting consulting services.
- **Scalable Architecture:** Easily extendable with Django apps and REST APIs if needed.

---

## Tech Stack

- **Backend:** [Django](https://www.djangoproject.com/) with Python 3.13
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** PostgreSQL

---

## Installation

### Prerequisites

- **Python 3.13:** Ensure you have Python 3.13 installed.
- **pip:** Python package installer.
- **virtualenv** (recommended): To create an isolated Python environment.

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/andojoks/bpdataconsulting.git
   cd bpdataconsulting
   ```

2. **Create and Activate a Virtual Environment:**

   Create a virtual environment to keep your dependencies isolated:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies:**

   Install all required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file from `.env.example` in the project root and fill with your configuration settings. :

   ```env

    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1

    # Database Configuration
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=5432
   ```

5. **Apply Migrations:**

   Set up your database by running:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser:**

   To access the Django admin interface, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

---

## Development

For local development, use Django’s built-in development server.

### Running the Development Server:

Start the server with:

```bash
python manage.py runserver
```

Then, open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the site.

---

## Production

For a production environment, it is recommended to use a robust WSGI server like Gunicorn.

### Steps for Production Deployment:

1. **Prepare Static Files:**

   Before deploying, collect all static files:

   ```bash
   python manage.py collectstatic
   ```

2. **Update environment variables:**
  
   Update the environment variables, by setting debug to false, and

## Contributing

We welcome contributions to this project. Please see the [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or feedback, please contact the developer at [andojoks@gmail.com](mailto:andojoks@gmail.com).