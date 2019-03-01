import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd!dom0bnas_$csrnmpd@gx==t6l_b++2#r@x=-7i=%^fs$brd!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1' ,'grievancesystem.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'grievance.apps.GrievanceConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
]
CRIPSY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Grievance_System.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Grievance_System/templates'],
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

WSGI_APPLICATION = 'Grievance_System.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ddgphbqn5irif',
        'USER':'yuvdkyhxoeskcf',
        'PASSWORD':'be9d9a5a3199c744de91d2ccfd20ab8c8677322d204ed3ca4d970d3409e650c1',
        'HOST':'ec2-54-235-134-25.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'


STATICFILES_DIRS = (os.path.join(BASE_DIR, "statics"),)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
#EMAIL_HOST ='smpt.gmail.com'
#EMAIL_HOST_USER ='kalyansingh277@gmail.com'
#EMAIL_HOST_PASSWORD = 'Timesofindia1234'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#ACCOUNT_EMAIL_VERIFICATION = 'none'
# SEND_GRID_API_KEY = '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'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'abhijeet2812'
# EMAIL_HOST_PASSWORD = 'Timesofindia1234'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'kalyansingh277'
EMAIL_HOST_PASSWORD = '277kalyan'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
