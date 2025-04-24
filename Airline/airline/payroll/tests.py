from django.test import TestCase

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline.settings')
# Create your tests here.

from django.test import TestCase
from .models import Employee, Payroll
from django.contrib.auth.models import User

# Test case for the Payroll app
class PayrollTestCase(TestCase):
    # Set up the test case
    def setUp(self): # method called before test
        # Create a test user and employee
        user = User.objects.create(username="testuser") # Create a test user
        employee = Employee.objects.create( # Create a test employee
            user=user,
            position="Pilot",
            salary=5000,
            date_hired="2023-01-01"  # Provide a valid date for date_hired
        )
        # Create a test payroll entry
        Payroll.objects.create( # Create a test payroll entry
            employee=employee, # Associate it with the test employee
            month="January",
            salary_paid=5000,
            deductions=500
        )

    # Test if the employee was created successfully
    def test_net_salary_calculation(self):
        payroll = Payroll.objects.get(month="January")  # Retrieve the payroll entry for January
        self.assertEqual(payroll.net_salary, 4500) # Check if the net salary is calculated correctly (5000 - 500 = 4500)