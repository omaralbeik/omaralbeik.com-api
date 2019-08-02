import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "SECRET_KEY"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = "GET"

RECAPTCHA_SECRET_KEY = "REPLACE_WITH_RECAPTCHA_SECRET_KEY"

CLIENT_PROD_URL = "https://example.com"

ADMIN_HEADER = "Website | Admin"
ADMIN_TITLE = "Website"
ADMIN_PAGE_TITLE = "Site Administration"
