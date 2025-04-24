# Airline Payroll Management System - Powered by Django
This is a school project I developed using Django. It serves as a payroll management system for an airline, allowing employees to view their payroll details and admins to manage payroll entries.

## Key Features
You can sign up and log in.
Employees can view their payroll details (salary, deductions, etc.).
Admins can add and manage payroll entries.
Includes automatic tests to ensure functionality.
Comes with a Django admin page for full control.

## User Roles
The Employee – logs in to view their payroll details.
The Admin – manages payroll entries and has full access.


## Technologies Used
Django 5.2 (runs the app)
Python 3.13
SQLite (Django’s built-in database)
HTML, CSS for the layout

## Setup Instructions
Download or clone the code:
git clone https://github.com/EliteSSSstar/Django.git
cd Django
Make a virtual environment and install dependencies:


python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

Set up the database:

py manage.py migrate
Make a superuser (admin):

py manage.py createsuperuser
Start the server:

py manage.py runserver
Open your browser and go to: http://127.0.0.1:8000/

## Running Tests
You can test the site like this:
py manage.py test

## Submitted Files
Design1_UseCases.pdf – has the use case diagram.
Design2_ERD.pdf – database diagram.
Design3_tests.zip – the test code in a zip file.

## Additional Notes
For my 3rd-year Web Framework Development module at TUD, I created this project. It’s a simple implementation, but the learning experience was invaluable!
