from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Vista de registro
    path('login/', views.login_view, name='login'),       # Vista de login
    path('dashboard/', views.dashboard, name='dashboard'), # Vista del dashboard
]
