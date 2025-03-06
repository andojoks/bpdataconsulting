# B&P Data Consulting

Welcome to the B&P Data Consulting website project. This application is built on the Django framework using Python 3.13 and serves as the foundational platform for bpdata Consulting’s online presence. The project is designed to efficiently support both development and production environments.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Development](#development)
- [Deployment](#deployment)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Responsive Design:** A mobile-first approach ensuring usability across all devices.
- **Admin Interface:** A robust Django admin for managing content and user data efficiently.
- **Authentication:** Secure user registration, login, and profile management.
- **Consulting Services:** Detailed pages and features highlighting the range of consulting services offered.
- **Scalable Architecture:** Easily extendable with Django apps and REST APIs as needed.
- **Security:** Built-in protections against common web vulnerabilities.

---

## Tech Stack

- **Backend:** [Django](https://www.djangoproject.com/) 3.2 with Python 3.8.10
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** PostgreSQL 10.3

---

## Installation

### Prerequisites

- **Python 3.8.10:** Ensure you have Python 3.8.10 installed.
- **pip:** Python package installer must be available. (version 22.3.1 recommended)
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

   Create a `.env` file from `.env.example` in the project root and populate it with your configuration settings:

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

5. **Make Migrations and apply Apply Then:**

  Generate any new migration files (if there are changes) and apply them to set up the database schema. run the following commands in succession.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser:**

   To access the Django admin interface, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

  Follow the prompts to enter your username, email, and password.
---

## Development

For local development, use Django’s built-in development server.

### Running the Development Server:

Start the server with:

```bash
python manage.py runserver
```

Then, open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the site. The admin interface is available at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  

---

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or feedback, please contact the developer at [andojoks@gmail.com](mailto:andojoks@gmail.com).