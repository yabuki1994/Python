from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
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
    # フォーマットの設定
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
    # ログ出力先の設定
    "handlers": {
        # コンソールに出力
        'console': {
            "formatter": "verbose",
            'class': 'logging.StreamHandler',
        },
        # ファイルに出力（アプリケーション）
        "user": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR ,"log","app.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 1,
            "backupCount": 5,
        },
        # ファイルに出力（システム）
        "system": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR ,"log", "system.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 1,
            "backupCount": 5,
        },
    },
    "loggers": {
        # アプリケーション用ログレベル（app_uswebフォルダ配下のファイルログ）
        "app_usweb": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "DEBUG"),
            "propagate": True,
        },
        # Framework用ログレベル（djangoライブラリにもともと設定されているログ）
        # とんでもねぇ量のlogが出るので必要に応じてLEVELを設定する
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "WARN"),
            "propagate": True,
        },
    },
}
