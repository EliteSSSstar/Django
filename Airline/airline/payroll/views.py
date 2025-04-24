
from django.shortcuts import render, redirect
from .models import Employee, Payroll # This imports the Employee and Payroll models from the models.py file
from .forms import PayrollForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# This view handles the homepage of the payroll app
@login_required
def homepage(request):
    return redirect('/admin/login/')

# payroll list and allows for adding new payroll entries
@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all() # This retrieves all payroll entries from the database
    return render(request, 'payroll/payroll_list.html', {'payrolls': payrolls}) # This renders the payroll list template with the retrieved payrolls

# This view handles the addition of new payroll entries
@login_required
def add_payroll(request):
    if request.method == 'POST': # This checks if the request method is POST, indicating that the form has been submitted
        form = PayrollForm(request.POST) # creates a new instance of the PayrollForm
        if form.is_valid():
            form.save() # This saves the new payroll entry to the database
            return redirect('payroll_list')  # This redirects to the payroll list view after saving
    else:
        form = PayrollForm() # This creates a new instance of the PayrollForm for rendering in the template
    return render(request, 'payroll/add_payroll.html', {'form': form})

@login_required # This decorator ensures that only logged-in users can access this view
def user_payroll(request): #
    payrolls = Payroll.objects.filter(employee__user=request.user) # This filters the payrolls to only include those associated with the logged-in user
    return render(request, 'payroll/user_payroll.html', {'payrolls': payrolls})