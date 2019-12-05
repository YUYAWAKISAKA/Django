import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY='1-hrok2*qb=2v9-(ppg37w@&52lel$2z47wws-_xs=i-(%#_hs'

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True #ローカルでDebugできるようになります
