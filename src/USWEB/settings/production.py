from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_app_db',
        'USER': 'djangouser',
        'PASSWORD': 'djangouser',
        'HOST': 'usc-12-1303',
        'PORT': '5432'
    }
}

"""
ログの設定
 DEBUG: デバッグのための低レベルシステム情報
 INFO: 一般的なシステム情報
 WARNING: 重要度の小さい問題が発生したことを示す情報
 ERROR: 大きな問題が発生したことを示す情報
 CRITICAL: 重大な問題が発生したことを示す情報
"""
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "\t".join(
                [
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(name)s.%(funcName)s:%(lineno)s",
                    "%(message)s",
                ]
            )
        },
    },
    "handlers": {
        'console': {
            "formatter": "verbose",
            'class': 'logging.StreamHandler',
        },
        "user": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR ,"log","app.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 1,
            "backupCount": 5,
        },
        "system": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR ,"log", "system.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 1,
            "backupCount": 5,
        },
    },
    "loggers": {
        # アプリケーション用ログレベル
        "app_usweb": {
            "handlers": ["user"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
        # Framework用ログレベル
        "django": {
            "handlers": ["system"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "ERROR"),
            "propagate": True,
        },
    },
}