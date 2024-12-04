# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), 
     path('', views.index, name='index'),# Incluye las rutas de la app 'users'
    # Otras rutas...
]
