import os
from pathlib import Path
from dotenv import load_dotenv
from dotenv import dotenv_values

# settings.py

## using existing module to specify location of the .env file
## from pathlib import Path
## import os

"""
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


# config = {"USER": "foo", "EMAIL": "foo@example.org"}
config = dotenv_values(".env")
"""


# retrieving keys and adding them to the project
# from the .env file through their key names
#SECRET_KEY = os.getenv("SECRET_KEY")
#DOMAIN = os.getenv("DOMAIN")
#EMAIL = os.getenv("EMAIL")

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

PORTF_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY='django-insecure-*lc$%ggly7vfv))lgn7@dv-0y6oep*#m!9vw@&o$2!4(b2^^6p'




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    
   "*"
   
    ]


# Application definition

INSTALLED_APPS = [
    'channels',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django.contrib.sites',
    'django.contrib.staticfiles',
    
 

    
    'rest_framework',
    'tailwind',
    'theme',
    



    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
   
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
)

ASGI_APPLICATION = "ecommerce.asgi.application"


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}



"""

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}

"""


TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

#LOGIN_URL = 

ROOT_URLCONF = 'ecommerce.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #BASE_DIR / 'portfolio/build'
        ],
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



REDIS_HOST = 'localhost'
REDIS_PORT = 6379


WSGI_APPLICATION = 'ecommerce.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    'default': env.db(),

    # read os.environ['SQLITE_URL']
    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////tmp/my-tmp-sqlite.db'
    )
}
"""

#AUTH_USER_MODEL = 'theme.MyUser'

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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


REDIS_URL = 'redis://localhost:6370'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

#STATIC_DIR = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = [STATIC_DIR, ]

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR / 'static/images')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Das Notes,, (#):
"""

You can run the Django command health_check to perform your health checks via the command line, or periodically with a cron, as follow:

django-admin health_check


_______


How django-defender works

When someone tries to login, we first check to see if they are currently blocked. We check the username they are trying to use, as well as the IP address. If they are blocked, goto step 5. If not blocked go to step 2.
They are not blocked, so we check to see if the login was valid. If valid go to step 6. If not valid go to step 3.
Login attempt wasn’t valid. Add their username and IP address for this attempt to the cache. If this brings them over the limit, add them to the blocked list, and then goto step 5. If not over the limit goto step 4.
Login was invalid, but not over the limit. Send them back to the login screen to try again.
User is blocked: Send them to the blocked page, telling them they are blocked, and give an estimate on when they will be unblocked.
Login is valid. Reset any failed login attempts, and forward to their destination.

____

The Guardian anonymous user is different from the Django Anonymous user. The Django Anonymous user does not have an entry in the database, however the Guardian anonymous user does.
#   This means that the following code will return an unexpected result:

from django.contrib.auth import get_user_model
User = get_user_model()
anon = User.get_anonymous()
anon.is_anonymous  # returns False

"""