import os
from pathlib import Path

# Definición de BASE_DIR para asegurar que apunta a la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad y configuración general
SECRET_KEY = 'tu-clave-secreta'  # Cambia esto por una clave secreta segura
DEBUG = True  # Cambia esto por False en producción
ALLOWED_HOSTS = []  # Define los hosts permitidos, como ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicaciones del proyecto
    'users',  # Aplicación de usuarios
    'transactions',  # Aplicación de transferencias
    'contracts',  # Aplicación de contratos
    'exchange',  # Aplicación de exchange
    'qa_system',  # Sistema de atención al cliente (si lo tienes implementado)
]

# Configuración de modelo de usuario personalizado
AUTH_USER_MODEL = 'users.CustomUser'

# Configuración de correo en Django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Usamos Gmail como ejemplo
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tuemail@gmail.com'  # Cambia esto por tu correo electrónico
EMAIL_HOST_PASSWORD = 'tucontraseña'  # Cambia esto por tu contraseña de aplicación de Gmail
DEFAULT_FROM_EMAIL = 'tuemail@gmail.com'  # El correo que se usará como remitente

# Configuración de archivos estáticos
STATIC_URL = '/static/'

# Ubicación de archivos estáticos adicionales (dentro de tu carpeta 'static' en el directorio raíz)
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ubicación de tus archivos estáticos en el proyecto
]

# Archivos de medios (imágenes, documentos subidos por los usuarios, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Rutas de las plantillas (templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ubicación de tus plantillas HTML
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de base de datos (SQLite como ejemplo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'crypto_exchange.urls'

# Configuración de WSGI
WSGI_APPLICATION = 'crypto_exchange.wsgi.application'

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración internacionalización y zona horaria
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de sesiones
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 3600  # Duración de la sesión en segundos (1 hora)

# Seguridad
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Configuración de logs (opcional)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Configuración para que Django use las aplicaciones de tu proyecto como parte de las URLs
# No olvides configurar las rutas en 'crypto_exchange/urls.py'
