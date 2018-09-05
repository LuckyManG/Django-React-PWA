"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import bcrypt
import raven
import dj_database_url

APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(APP_DIR)
SRC_DIR = os.path.dirname(BASE_DIR)
PROJECT_DIR = os.path.dirname(SRC_DIR)
WEBPACK_STAT_DIR = os.path.join(SRC_DIR, 'client')
REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', bcrypt.gensalt())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEV') == 'True'
DEBUG_404 = True
TESTING = "pytest" in sys.modules

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'noelwilson2018.herokuapp.com',
    'noel-wilson-2018.herokuapp.com',
    'www.noel-wilson.co.uk',
    'www.jwnwilson.com',
    'noel-wilson.co.uk',
    'jwnwilson.com',
]


# Application definition
INSTALLED_APPS = [
    'raven.contrib.django.raven_compat',
    'rest_framework',
    'wagtail.api.v2',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'polymorphic',
    'webpack_loader',
    'webapp.cms',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'webapp.cms.middleware.RenderTronMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if os.environ.get('ON_HEROKU'):
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
elif TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'noelwilson2018',
            'USER': 'docker',
            'PASSWORD': 'docker',
            'HOST': 'db',  # set in docker-compose.yml
            'PORT': 5432  # default postgres port
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True
WAGTAIL_APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(APP_DIR, 'static'),
    os.path.join(SRC_DIR, 'client', 'build', 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WAGTAIL_SITE_NAME = 'Noel Wilson'

if DEBUG:
    WEBPACK_LOADER = {
        'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(WEBPACK_STAT_DIR, 'webpack-stats.dev.json'),
        }
    }
else:
    WEBPACK_LOADER = {
        'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(WEBPACK_STAT_DIR, 'webpack-stats.prod.json'),
        }
    }

if not DEBUG and not TESTING:
    RAVEN_CONFIG = {
        'dsn': 'https://4455bc30a01746f6ad07e8bb17fdcb7e:244d3d07cc2641b09cfede93ef8dad8e@sentry.io/646552',
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': os.environ['SOURCE_VERSION'] if os.environ.get('ON_HEROKU') else raven.fetch_git_sha(PROJECT_DIR)
    }

# Setup throwaway email address to send emails
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jwnwilsonemail@gmail.com'
EMAIL_HOST_PASSWORD = 'Jwnwilson1'

# Setup caching
def get_cache():
    """
    Heroku specific caching settings
    """
    if os.environ.get('ON_HEROKU'):
        try:
            servers = os.environ['MEMCACHIER_SERVERS']
            username = os.environ['MEMCACHIER_USERNAME']
            password = os.environ['MEMCACHIER_PASSWORD']
            return {
              'default': {
                'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                # TIMEOUT is not the connection timeout! It's the default expiration
                # timeout that should be applied to keys! Setting it to `None`
                # disables expiration.
                'TIMEOUT': None,
                'LOCATION': servers,
                'OPTIONS': {
                  'binary': True,
                  'username': username,
                  'password': password,
                  'behaviors': {
                    # Enable faster IO
                    'no_block': True,
                    'tcp_nodelay': True,
                    # Keep connection alive
                    'tcp_keepalive': True,
                    # Timeout settings
                    'connect_timeout': 2000,  # ms
                    'send_timeout': 750 * 1000,  # us
                    'receive_timeout': 750 * 1000,  # us
                    '_poll_timeout': 2000,  # ms
                    # Better failover
                    'ketama': True,
                    'remove_failed': 1,
                    'retry_timeout': 2,
                    'dead_timeout': 30,
                  }
                }
              }
            }
        except:
            return {
                'default': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
                }
            }
    else:
        return {
            # Memecached + docker + Mac OS has terrible performance
            # 'default': {
            #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            #     'LOCATION': 'memcached:11211'
            # }
            # 'default': {
            #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            #     'LOCATION': 'noelwilson2018'
            # }
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": REDIS_URL,
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient"
                },
                "KEY_PREFIX": "noelwilson2018"
            }
        }

CACHES = get_cache()

# AWS stuff
if os.environ.get('ON_HEROKU'):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = 'noel-wilson.co.uk'
    AWS_ACCESS_KEY_ID = os.environ.get('ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('SECRET')
    AWS_QUERYSTRING_AUTH = False

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures')
]

if TESTING:
    DEBUG = False

# Celery stuff
CELERY_BROKER_URL = REDIS_URL
BROKER_URL = REDIS_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 60

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        }
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    },
}

