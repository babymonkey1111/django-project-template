from settings.base import *


DEBUG = False

ALLOWED_HOSTS = ['{{cookiecutter.repo_name|as_hostname}}.{{cookiecutter.test_host}}']

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = 'https://{{cookiecutter.repo_name|as_hostname}}.{{cookiecutter.test_host}}'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_HOST_PASSWORD = 'TODO (api key)'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_URL = '/assets/'

# Production logging - all INFO and higher messages go to info.log file. ERROR and higher messages additionally go to
#  error.log file plus to Sentry.
LOGGING['handlers'] = {
    'info_log': {
        'level': 'INFO',
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': '/var/log/{{cookiecutter.repo_name}}/info.log',
        'formatter': 'default',
    },
    'error_log': {
        'level': 'ERROR',
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': '/var/log/{{cookiecutter.repo_name}}/error.log',
        'formatter': 'default',
    },
    'sentry': {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    },
}
LOGGING['loggers'][''] = {
    'handlers': ['info_log', 'error_log', 'sentry'],
    'level': 'INFO',
    'filters': ['require_debug_false'],
}

# Sentry error logging
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)
RAVEN_BACKEND_DSN = 'https://TODO:TODO@sentry.thorgate.eu/TODO'
RAVEN_PUBLIC_DSN = 'https://TODO@sentry.thorgate.eu/TODO'
RAVEN_CONFIG['dsn'] = RAVEN_BACKEND_DSN

# Enable {{ cookiecutter.django_media_engine }} storage
DEFAULT_FILE_STORAGE = '{{ cookiecutter.repo_name }}.storages.MediaStorage'
MEDIA_ROOT = ''
{% if cookiecutter.django_media_engine == 'S3' -%}
AWS_STORAGE_BUCKET_NAME = '{{ cookiecutter.repo_name }}-staging'
AWS_ACCESS_KEY_ID = None  # set in local.py
AWS_SECRET_ACCESS_KEY = None  # set in local.py
{%- endif %}{% if cookiecutter.django_media_engine == 'GCS' -%}
GS_BUCKET_NAME = '{{ cookiecutter.repo_name }}-staging'
GS_PROJECT_ID = None  # set in local.py
GS_CREDENTIALS = None  # set in local.py{% endif %}
