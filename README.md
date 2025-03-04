# Task Manager Project

## Overview
This is a Django project for managing tasks. It includes functionality for creating, editing, deleting, and searching tasks.

## Setup Instructions

### Installation Requirements
- Python 3.x
- Django 3.x
- PHPMYSQl (updated version, activate apache and mysql)



### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nestyy315/DjangoProject.git
    cd task-manager
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. **Set up the database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.



