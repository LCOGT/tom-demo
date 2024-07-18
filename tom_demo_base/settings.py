"""
Django settings for your TOM project.

Originally generated by 'django-admin startproject' using Django 2.1.1.
Generated by ./manage.py tom_setup on Feb. 18, 2020, 7:38 p.m.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import tempfile

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!hrpq+h(_n!ml847_!0h6hi8+1y0t&amp;#%&amp;eo_^=#yd6af_!+cf2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('TOM_DEMO_DEBUG', False)

ALLOWED_HOSTS = ['*']


# Application definition
TOM_NAME = 'TOM Demo'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'guardian',
    'tom_common',
    'django_comments',
    'bootstrap4',
    'crispy_bootstrap4',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'django_gravatar',
    'tom_targets',
    'tom_alerts',
    'tom_catalogs',
    'tom_observations',
    'tom_dataproducts',
    'tom_swift',
    'tom_hermes',
    'tom_fink',
    'tom_dataservices',
    'tom_tns',
    'tom_demo'
]

# TODO: please explain why this is necessary. what error does it prevent?
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tom_common.middleware.Raise403Middleware',
    'tom_common.middleware.ExternalServiceMiddleware',
    'tom_common.middleware.AuthStrategyMiddleware',
]

ROOT_URLCONF = 'tom_demo_base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'tom_demo_base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
       'NAME': os.getenv('DB_NAME', 'tom_demo'),
       'USER': os.getenv('DB_USER', 'postgres'),
       'PASSWORD': os.getenv('DB_PASS', 'postgres'),
       'HOST': os.getenv('DB_HOST', '127.0.0.1'),
       'PORT': os.getenv('DB_PORT', '5432'),
   },
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
# ]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = r'^/(api)/.*$|^/o/.*'
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1',
    'http://*',
    'https://*',
    'https://tom-demo.lco.global'
]
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:80',
    'http://*',
    'https://*',
    'https://tom-demo.lco.global'
]
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = 'Y-m-d H:m:s'
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'data')
MEDIA_URL = '/data/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}

# Caching
# https://docs.djangoproject.com/en/dev/topics/cache/#filesystem-caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': tempfile.gettempdir()
    }
}

# AWS S3 Data Storage configuration

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_S3_BUCKET', '')
# AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'us-west-2')
# AWS_DEFAULT_ACL = None

# TOM Specific configuration
TARGET_TYPE = 'SIDEREAL'

TARGET_MODEL_CLASS = 'tom_demo.models.UserDefinedTarget'

# These are the facilities that will be available on the TargetDetail page Observe tab
# i.e. the facilities to which you can submit an observation request.
TOM_FACILITY_CLASSES = [
    'tom_observations.facilities.lco.LCOFacility',
    'tom_observations.facilities.gemini.GEMFacility',
    'tom_observations.facilities.soar.SOARFacility',
    'tom_observations.facilities.lt.LTFacility',
    'tom_swift.swift.SwiftFacility'
]

# This is the configuration dictionary (of dictionaries) for the facilities
# listed above in the TOM_FACILITY_CLASSES list.
FACILITIES = {
    'LCO': {
        'portal_url': 'https://observe.lco.global',
        'api_key': '',
    },
    'GEM': {
        'portal_url': {
            'GS': 'https://139.229.34.15:8443',
            'GN': 'https://128.171.88.221:8443',
        },
        'api_key': {
            'GS': '',
            'GN': '',
        },
        'user_email': '',
        'programs': {
            'GS-YYYYS-T-NNN': {
                'MM': 'Std: Some descriptive text',
                'NN': 'Rap: Some descriptive text'
            },
            'GN-YYYYS-T-NNN': {
                'QQ': 'Std: Some descriptive text',
                'PP': 'Rap: Some descriptive text',
            },
        },
    },
    'SWIFT': {
        'SWIFT_USERNAME': os.getenv('SWIFT_USERNAME', 'anonymous'),
        'SWIFT_SHARED_SECRET': os.getenv('SWIFT_SHARED_SECRET', 'anonymous'),
    },
}

# Define the valid data product types for your TOM. Be careful when removing items, as previously valid types will no
# longer be valid, and may cause issues unless the offending records are modified.
DATA_PRODUCT_TYPES = {
    'photometry': ('photometry', 'Photometry'),
    'fits_file': ('fits_file', 'FITS File'),
    'spectroscopy': ('spectroscopy', 'Spectroscopy'),
    'image_file': ('image_file', 'Image File')
}

DATA_PROCESSORS = {
    'photometry': 'tom_dataproducts.processors.photometry_processor.PhotometryProcessor',
    'spectroscopy': 'tom_dataproducts.processors.spectroscopy_processor.SpectroscopyProcessor',
}

DATA_SHARING = {
    'hermes': {
        'DISPLAY_NAME': os.getenv('HERMES_DISPLAY_NAME', 'Hermes'),
        'BASE_URL': os.getenv('HERMES_BASE_URL', 'https://hermes.lco.global/'),
        'SCIMMA_AUTH_USERNAME': os.getenv('SCIMMA_AUTH_USERNAME', None),
        'CREDENTIAL_USERNAME': os.getenv('SCIMMA_CREDENTIAL_USERNAME', None),
        'CREDENTIAL_PASSWORD': os.getenv('SCIMMA_CREDENTIAL_PASSWORD', None),
        'USER_TOPICS': ['hermes.test', 'tomtoolkit.test']
    },
}

ALERT_STREAMS = [
    {
        'ACTIVE': True,
        'NAME': 'tom_alertstreams.alertstreams.hopskotch.HopskotchAlertStream',
        'OPTIONS': {
            'URL': 'kafka://kafka.scimma.org/',
            'USERNAME': os.getenv('SCIMMA_CREDENTIAL_USERNAME', None),
            'PASSWORD': os.getenv('SCIMMA_CREDENTIAL_PASSWORD', None),
            # The hop-client requires that the GROUP_ID prefix match the SCIMMA_AUTH_USERNAME
            'GROUP_ID': os.getenv('SCIMMA_CREDENTIAL_USERNAME', "") + '-' +
                        os.getenv('HOPSKOTCH_GROUP_ID', 'tom-demo-dev' if DEBUG else 'tom-demo'),
            'TOPIC_HANDLERS': {
                'sys.heartbeat': 'tom_alertstreams.alertstreams.hopskotch.heartbeat_handler',
                'tomtoolkit.test': 'tom_dataproducts.alertstreams.hermes.hermes_alert_handler',
                'hermes.test': 'tom_dataproducts.alertstreams.hermes.hermes_alert_handler',
                'igwn.gwalert': 'tom_nonlocalizedevents.alertstream_handlers.igwn_event_handler.handle_igwn_message',
            },
        },
    },
    {
        'ACTIVE': False,
        'NAME': 'tom_alertstreams.alertstreams.gcn.GCNClassicAlertStream',
        # The keys of the OPTIONS dictionary become (lower-case) properties of the AlertStream instance.
        'OPTIONS': {
            # see https://github.com/nasa-gcn/gcn-kafka-python#to-use for configuration details.
            'GCN_CLASSIC_CLIENT_ID': os.getenv('GCN_CLASSIC_CLIENT_ID', None),
            'GCN_CLASSIC_CLIENT_SECRET': os.getenv('GCN_CLASSIC_CLIENT_SECRET', None),
            'DOMAIN': 'gcn.nasa.gov',  # optional, defaults to 'gcn.nasa.gov'
            'CONFIG': {  # optional
                'group.id': 'tom-demo-dev.lco.gtn' if DEBUG else 'tom-demo.lco.global',
                # 'auto.offset.reset': 'earliest',
                # 'enable.auto.commit': False
            },
            'TOPIC_HANDLERS': {
                'gcn.classic.text.LVC_INITIAL': 'tom_nonlocalizedevents.alertstream_handlers.gw_event_handler.handle_message',
                'gcn.classic.text.LVC_PRELIMINARY': 'tom_nonlocalizedevents.alertstream_handlers.gw_event_handler.handle_message',
                'gcn.classic.text.LVC_RETRACTION': 'tom_nonlocalizedevents.alertstream_handlers.gw_event_handler.handle_retraction',
            },
        },
    }
]

TOM_ALERT_CLASSES = [
    'tom_alerts.brokers.alerce.ALeRCEBroker',
    # 'tom_alerts.brokers.antares.ANTARESBroker',
    'tom_alerts.brokers.gaia.GaiaBroker',
    'tom_hermes.hermes.HermesBroker',
    'tom_alerts.brokers.gaia.GaiaBroker',
    'tom_alerts.brokers.lasair.LasairBroker',
    'tom_alerts.brokers.scout.ScoutBroker',
    'tom_alerts.brokers.tns.TNSBroker',
    'tom_fink.fink.FinkBroker',
    'tom_dataservices.data_services.lsst.RSPMultiTargetDataService'
]

TOM_ALERT_DASH_CLASSES = [
    #'tom_alerts_dash.brokers.mars.MARSDashBroker',
    # 'tom_alerts_dash.brokers.alerce.ALeRCEDashBroker',
    #'tom_alerts_dash.brokers.scimma.SCIMMADashBroker'
]

TOM_HARVESTER_CLASSES = [
    'tom_catalogs.harvesters.simbad.SimbadHarvester',
    'tom_catalogs.harvesters.ned.NEDHarvester',
    'tom_catalogs.harvesters.jplhorizons.JPLHorizonsHarvester',
    'tom_catalogs.harvesters.tns.TNSHarvester',
]

BROKERS = {
    'LASAIR': {
        'api_key': os.getenv('LASAIR_API_KEY', ''),
    },
    'TNS': {
        'api_key': os.getenv('TNS_API_KEY', ''),
        'bot_id': os.getenv('TNS_BOT_ID', '165852'),
        'bot_name': os.getenv('TNS_BOT_NAME', 'TOM_BOT'),
        'tns_base_url': 'https://sandbox.wis-tns.org/api',  # Note this is the Sandbox URL
        'group_name': os.getenv('TNS_GROUP_NAME', 'Hermes_group'),
        'default_authors': 'Foo Bar <foo@bar.com>, Rando Calrissian, et al.',
    },
}

# Define extra target fields here. Types can be any of "number", "string", "boolean" or "datetime"
# See https://tomtoolkit.github.io/docs/target_fields for documentation on this feature
# For example:
# EXTRA_FIELDS = [
#     {'name': 'redshift', 'type': 'number'},
#     {'name': 'discoverer', 'type': 'string'}
#     {'name': 'eligible', 'type': 'boolean'},
#     {'name': 'dicovery_date', 'type': 'datetime'}
# ]
EXTRA_FIELDS = []

# Authentication strategy can either be LOCKED (required login for all views)
# or READ_ONLY (read only access to views)
AUTH_STRATEGY = 'READ_ONLY'

TARGET_PERMISSIONS_ONLY = False

# URLs that should be allowed access even with AUTH_STRATEGY = LOCKED
# for example: OPEN_URLS = ['/', '/about']
OPEN_URLS = []

HOOKS = {
    'target_post_save': 'tom_common.hooks.target_post_save',
    'observation_change_state': 'tom_common.hooks.observation_change_state',
    'data_product_post_upload': 'tom_dataproducts.hooks.data_product_post_upload'
}

AUTO_THUMBNAILS = False

THUMBNAIL_MAX_SIZE = (0, 0)

THUMBNAIL_DEFAULT_SIZE = (200, 200)

HINTS_ENABLED = True
HINT_LEVEL = 20

#
# tom_nonlocalizedevents configuration
#

HERMES_API_URL = os.getenv('HERMES_API_URL', 'https://hermes.lco.global')

# both tom_nonlocalized events and tom_hermes use HERMES_API_URL
# first, try to get its value from the environment, otherwise use the settings.DEBUG var to determine
# its value. settings.DEBUG is set above according to TOM_DEMO_DEBUG, which is set in the
# helm-chart/values*.yaml files (and injected into the env via _helpers.tpl)
# So, tom-demo-dev will use hermes-dev and tom-demo will use hermes
HERMES_API_URL = os.getenv('HERMES_API_URL',
                           'https://hermes-dev.lco.global' if DEBUG else 'https://hermes.lco.global')

VUE_FRONTEND_DIR = os.path.join(STATIC_ROOT, 'vue')  # I don't think this is actually used...
VUE_FRONTEND_DIR_TOM_NONLOCAL = os.path.join(STATIC_ROOT, 'tom_nonlocalizedevents/vue')
VUE_FRONTEND_DIR_TOM_DEMO = os.path.join(STATIC_ROOT, 'tom_demo/vue')
WEBPACK_LOADER = {
    'TOM_NONLOCALIZEDEVENTS': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'tom_nonlocalizedevents/vue/',  # must end with slash
        'STATS_FILE': os.path.join(VUE_FRONTEND_DIR_TOM_NONLOCAL, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    },
    'TOM_DEMO': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'tom_demo/vue/',  # must end with slash
        'STATS_FILE': os.path.join(VUE_FRONTEND_DIR_TOM_DEMO, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

try:
    from local_settings import *  # noqa
except ImportError:
    pass
