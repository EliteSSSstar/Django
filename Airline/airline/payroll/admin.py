from django.contrib import admin

from .models import Employee, Payroll

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'salary', 'date_hired')
    search_fields = ('user__username', 'position')


# Register Payroll model
@admin.register(Payroll) # This decorator registers the Payroll model with the admin site
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'salary_paid', 'deductions', 'net_salary')
    search_fields = ('employee__user__username', 'month')
    list_filter = ('month',)