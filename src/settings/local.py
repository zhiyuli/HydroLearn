import os
print("***In Local Settings")

# ************************SECURITY SETTINGS************************************
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


print('****************************** IN DEBUG:', DEBUG)

'''
    Dev settings
'''
SECRET_KEY = 's(fwbwrr##yn8r_cyjst5i^pjft^_5-%47m@^18xc@h+mz9f+^'

ALLOWED_HOSTS = ['example.com','HydroLearn.org', 'localhost', '127.0.0.1', '[::1]']
CSRF_COOKIE_SECURE = True


# CORS_REPLACE_HTTPS_REFERER = True
# HOST_SCHEME = 'https://'
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = True
# SECURE_FRAME_DENY = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}


# used for django_extensions' pydot rendering of DB schema
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

