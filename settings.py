INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',  # Aplicación de usuarios
    'transactions',  # Aplicación de transferencias
    'contracts',# Aplicación de contratos
    'exchange'# 
]
AUTH_USER_MODEL = 'users.CustomUser'
