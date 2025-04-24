

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Define the models for the payroll system
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_hired = models.DateField()

    def __str__(self):
        return self.user.username

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.net_salary = self.salary_paid - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.user.username} - {self.month}"
