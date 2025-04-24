from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth_views
from . import views

urlpatterns = [ # URL patterns for the payroll app
    path('', views.homepage, name='homepage'),
    path('login/', auth_views.LoginView.as_view(), name='login'), # Login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Logout view
    path('user/payroll/', views.user_payroll, name='user_payroll'), # User-specific payroll view
]