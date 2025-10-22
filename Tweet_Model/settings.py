from pathlib import Path
import os
import dj_database_url  # For Render-friendly database URL

# -----------------------------
# Base directories
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Security
# -----------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-zk^15fi=9497s5_j58=s0t%80vsz(h-v3qnfg3d5s^e#vx%e1o"
)

DEBUG = os.environ.get("RENDER", None) is None  # Turn off debug on Render

ALLOWED_HOSTS = ["tweet-model.onrender.com", "127.0.0.1", "localhost"]

# -----------------------------
# Applications
# -----------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tweet",  # your app
    "django_bootstrap5",  # optional
]

# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # for static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Tweet_Model.urls"

# -----------------------------
# Templates
# -----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Tweet_Model.wsgi.application"

# -----------------------------
# Database (Render-friendly)
# -----------------------------
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"), conn_max_age=600
    )
}

# -----------------------------
# Password validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------
# Internationalization
# -----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -----------------------------
# Static files (CSS, JS)
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -----------------------------
# Media files (uploaded images)
# -----------------------------
# For Render, use Persistent Disk at /mnt/media
MEDIA_URL = "/media/"
MEDIA_ROOT = Path("/mnt/media")  # Mount your persistent disk here

# -----------------------------
# Security settings for HTTPS
# -----------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = not DEBUG

# -----------------------------
# Login/Logout redirects
# -----------------------------
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "tweet_list"
LOGOUT_REDIRECT_URL = "login"

# -----------------------------
# Default primary key field
# -----------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
