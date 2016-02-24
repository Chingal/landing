
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ofbma5up(tx)e!!kzvx0_ev2z&way5@15fgiaji3$^p!dw51n3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Aplicaciones del core de Django
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Aplicaciones de Terceros
THIRD_PARTY_APPS = (
    'south',
)

# Aplicaciones Locales
LOCAL_APPS = (
    'landing.apps.signups',
)

# Aplicaciones Instaladas
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'landing.urls'

WSGI_APPLICATION = 'landing.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'landing.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Templates Dirs
TEMPLATE_DIRS = ( os.path.join(BASE_DIR, 'landing/templates'))

if DEBUG:
    # Media Files
    MEDIA_URL  = '/media/'
    MEDIA_ROOT =  os.path.join(BASE_DIR,'landing/media')
    STATIC_ROOT =  os.path.join(BASE_DIR,'landing/static')
    STATICFILES_DIRS = ( os.path.join( BASE_DIR, 'landing/static-local' ), )