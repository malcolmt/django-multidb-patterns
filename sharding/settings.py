import os

PROJ_ROOT = os.path.abspath(os.path.dirname(__file__))
DEV_MODE = True     # Used to control local static content serving.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS

# IMPORTANT: We cannot change the number of databases in the cluster after data
# has been stored (without dumping and reloading the data), as this would
# change the hashed locations for the pk values.
CLUSTER_SIZE = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db-main.sqlite',
        },
}
for db_num in range(CLUSTER_SIZE):
    name = "reviews-%s" % (db_num + 1)
    DATABASES[name] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db-%s.sqlite' % name,
        }

DATABASE_ROUTERS = ["reviews.router.ReviewRouter"]

TIME_ZONE = None
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ""

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/static/"

ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = 'e#4xobf8v8po82y=rhd3zjhq*@s$j82&l5m#e4v%s^r&nq$-l%'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'main_urls'
TEMPLATE_DIRS = (
    os.path.join(PROJ_ROOT, "..", "templates"),
)
FIXTURE_DIRS = (
    os.path.join(PROJ_ROOT, "..", "fixtures"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    "products",
    "reviews",
    "ticketing",
)

