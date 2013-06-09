# Django settings for pyheroes project.

from django.conf import global_settings
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pyheroes',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        }
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/vagrant/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/vagrant/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l%ylud)^owu*fb_hwrn@3!g!1zl_b=9sm(0m%%wiy@fzmi6*%0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.templates.loaders.eggs.Loader',
)

# MIDDLEWARE_CLASSES = (
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     # Uncomment the next line for simple clickjacking protection:
#     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )

MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES + (
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    # 'debug_toolbar.panels.profiling.ProfilingDebugPanel',
)

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2', '::ffff:10.0.2.2', )

ROOT_URLCONF = 'pyheroes.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pyheroes.wsgi.application'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'base',
    'hero',
    'home',
    'career',
    'item',
    'klass',
    'ranklist',
    'api',
    'task',

    'south' ,
    'debug_toolbar',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# --------------------------------------------------------------
# own settings
EUROPE = 1
AMERICA = 2
ASIA = 3
REGIONS = (
    (EUROPE, 'Europe'),
    (AMERICA, 'United States'),
    (ASIA, 'Asia'),
)

REGION_ABBREVIATIONS = (
    (EUROPE, 'eu'),
    (AMERICA, 'us'),
    (ASIA, 'as'),
)

HEROSCORE = 1
DPS = 2
LIFE = 3
ARMOR = 4
STRENGTH = 5
INTELLIGENCE = 6
DEXTERITY = 7
VITALITY = 8
ARCANE_RESIST = 9
FIRE_RESIST = 10
LIGHTNING_RESIST = 11
POISON_RESIST = 12
COLD_RESIST = 13
LIFE_STEAL = 15
LIFE_PER_KILL = 16
LIFE_ON_HIT = 17
ELITE_KILLS = 21


HEROSCORE = 'heroscore'
DPS = 'dps'
LIFE = 'life'
ARMOR = 'armor'
STRENGTH = 'strength'
INTELLIGENCE = 'intelligence'
DEXTERITY = 'dexterity'
VITALITY = 'vitality'
ARCANE_RESIST = 'arcaneresist'
FIRE_RESIST = 'fireresist'
LIGHTNING_RESIST = 'lightningresist'
POISON_RESIST = 'poisionresist'
COLD_RESIST = 'coldresist'
LIFE_STEAL = 'lifesteal'
LIFE_PER_KILL = 'lifeperkill'
LIFE_ON_HIT = 'lifeonhit'
ELITE_KILLS = 'elitekills'

# RANKLISTS = (
#     (HEROSCORE, 'heroscore'),
#     (DPS, 'dps'),
#     (LIFE, 'life'),
#     (ARMOR, 'armor'),
#     (STRENGTH, 'strength'),
#     (INTELLIGENCE, 'intelligence'),
#     (DEXTERITY, 'dexterity'),
#     (VITALITY, 'vitality'),
#     (ARCANE_RESIST, 'arcaneresist'),
#     (FIRE_RESIST, 'fireresist'),
#     (LIGHTNING_RESIST, 'lightningresist'),
#     (POISON_RESIST, 'poisionresist'),
#     (COLD_RESIST, 'coldresist'),
#     (LIFE_STEAL, 'lifesteal'),
#     (LIFE_PER_KILL, 'lifeperkill'),
#     (LIFE_ON_HIT, 'lifeonhit'),
#     (ELITE_KILLS, 'elitekills'),
# )

RANKLISTS = (
    HEROSCORE,
    DPS,
    LIFE,
    ARMOR,
    STRENGTH,
    INTELLIGENCE,
    DEXTERITY,
    VITALITY,
    ARCANE_RESIST,
    FIRE_RESIST,
    LIGHTNING_RESIST,
    POISON_RESIST,
    COLD_RESIST,
    LIFE_STEAL,
    LIFE_PER_KILL,
    LIFE_ON_HIT,
    ELITE_KILLS,
)

MINIMUM_RANK_LEVEL = 60