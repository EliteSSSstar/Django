from django import forms
from .models import Payroll

# This file contains the forms for the payroll app
class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll # model that the form is based on
        fields = ['employee', 'month', 'salary_paid', 'deductions'] # fields that will be in the form
