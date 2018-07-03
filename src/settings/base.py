import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 1.8.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os

print("***In Base Settings")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# ************************SECURITY SETTINGS************************************


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = bool(os.environ.get('DJANGO_DEBUG'))

#print('****************************** IN DEBUG:', DEBUG)

# Application definition
ROOT_URLCONF = 'src.urls'
WSGI_APPLICATION = 'src.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# directory to place static files on collection action
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_files')

# directories to check for static files
STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'src', 'static'),
    os.path.join(BASE_DIR, 'static'),
    #'/var/www/static',

)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_files')


SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/manage/'

ATOMIC_REQUESTS = True
# Mail is sent using the SMTP host and port specified in the
# EMAIL_HOST and EMAIL_PORT settings.

# The EMAIL_HOST_USER and EMAIL_HOST_PASSWORD settings,
# if set, are used to authenticate to the
# SMTP server, and the EMAIL_USE_TLS and EMAIL_USE_SSL settings control
# whether a secure connection is used.


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'src', 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',

            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    # testing the following
    #'django.middleware.security.SecurityMiddleware'

)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    # include custom User from accounts app before loading the cms
    'accounts',
    # OAuth client
    'social_django',

    # add in the django-cms apps
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',

    # include django extensions
    'django_extensions',

    # include polymorphism support
    'polymorphic',

    # admin element sorting extension
    'adminsortable2',

    # easy select 2 (filtered multiselect dropdown field for admin)
    'easy_select2',

    # tagging support
    'taggit',

    # ***************** include app installations
    'src',
    'src.apps.core',
    'src.apps.manage',
    'src.apps.module',
    'src.apps.tags',

)

# AUTH_USER_MODEL = 'accounts.User'
# SOCIAL_AUTH_USER_MODEL = 'accounts.User'

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('layout.html', 'HYDROLEARN_TEMPLATE'),
    ('home.html', 'HOME_TEMPLATE'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'module_intro': {
        'plugins': ['TextPlugin', ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': 'This module\'s introduction doesn\'t appear to have any content.',
                }
            }
        ]
    },

    'topic_summary': {
        'plugins': ['TextPlugin', ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': 'This topic\'s summary doesn\'t appear to have any content.',
                }
            }
        ]
    },

    'lesson_summary': {
        'plugins': ['TextPlugin', ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': 'This lesson\'s summary doesn\'t appear to have any content.',
                }
            }
        ]
    },

    'reading_content': {
        'plugins': ['TextPlugin', ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': 'This Reading Section doesn\'t appear to have any content.',
                }
            }
        ]
    },

    'activity_content': {
        'plugins': ['TextPlugin', ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': 'This Activity Section doesn\'t appear to have any content.',
                }
            }
        ]
    },

    'question_text': {
        'plugins': ['TextPlugin', ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': 'This Question hasn\'t been populated yet! Please add the question content!',
                }
            }
        ]
    },

    'answer_text': {
        'plugins': ['TextPlugin', ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': 'This Answer hasn\'t been populated yet! Please add the answer content!',
                }
            }
        ]
    },

}

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

MIGRATION_MODULES = {

}

THUMBNAIL_QUALITY = 95
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

THUMBNAIL_SUBDIR = 'thumbnails'

# CKeditor settings (adding style elements to content dropdown)
CKEDITOR_SETTINGS = {
    # 'language': '{{ language }}',
    # 'toolbar': 'CMS',
    # 'skin': 'moono',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'HorizontalRule', "-", 'Subscript', 'Superscript', '-', 'Blockquote',
         'RemoveFormat'],

        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['Link', 'Unlink'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],

    # See: https://github.com/yakupadakli/django_blog/blob/master/ckeditor/ckeditor/styles.js
    # for default style definitions.
    'stylesSet': [

        {
            'name': 'Main Section Header',
            'element': 'h2',
            'attributes': {
                'class': 'lesson-header',
            }
        },
        {
            'name': 'Subsection Header',
            'element': 'h3',
            'attributes': {
                'class': 'lesson-subheader',
            }
        },
        {
            'name': 'body text',
            'element': 'p',
        },

    ]
}

CKEDITOR_SETTINGS_OverlayImg = {
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['Format', 'Styles'],
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
    ]
}


SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_SLUGIFY_USERNAMES = True
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/manage/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/accounts/login/'


AUTHENTICATION_BACKENDS = (
    'accounts.hydroshare_oauth.HydroShareOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)