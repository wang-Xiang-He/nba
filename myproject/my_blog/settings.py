"""
Django settings for my_blog project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2bu%f4#=#*()lefw8_66+&ccgnha%+lj-f_07brez04g3oqgi2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	# 'channels',
    'article',
    'userprofile',
    'orders',
    'comment',
    'notice',
    # 'stock',
    'shop',
    'payment',
    'cart',
    # 'chat',
    'news',
    'nba',
    'taggit',
    'ckeditor',
    'mptt',
    'notifications',
    'password_reset',
     #django-allauth必须安装的app
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #第三方账号相关，根据需求添加
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github'
    # https://github.com/settings/applications/new

]

# channels
# 指定ASGI的路由地址
# ASGI_APPLICATION = 'my_blog.routing.application'


AUTHENTICATION_BACKENDS = (
      # django admin所使用的用户登录与django-allauth无关
      'django.contrib.auth.backends.ModelBackend',
      # allauth 身份验证
      'allauth.account.auth_backends.AuthenticationBackend',
)

#app django.contrib.sites需要的设置
SITE_ID = 1
# 指定要使用的登录方法(用户名、电子邮件地址两者之一)
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True

#第三方发送邮件
# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# # MAILGUN_ACCESS_KEY='pubkey-97ec101d5207bbf68160f82af10f1b82'#上图所示
# # MAILGUN_SERVER_NAME='sandbox38e9e90da12e4e65ad41477e61669e18.mailgun.org'#你的domain
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'a102204022@gmail.com'
# # LOGIN_REDIRECT_URL = '/article/article-list'
# LOGIN_REDIRECT_URL = '/'
# DEFAULT_FROM_EMAIL = '翔禾 <a102204022@gmail.com>'
# EMAIL_HOST_PASSWORD = 'rlxizckyvaqvaays'
# # from django.core.mail import send_mail
# # send_mail('MailGun works great!', 'It really really does.', 'postermaster@YOURHOST.com', ['YOUREMAIL@gmail.com'], fail_silently=False)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_blog.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

PythonAnywhere = False
if PythonAnywhere is False:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}}
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'myblog',
#             'USER': 'root',
#             'PASSWORD': 'a123456',
#             'HOST': 'localhost',
#             'PORT': '3306',
#         }
#     }
# elif PythonAnywhere is True:
#     DEBUG = False
#     ALLOWED_HOSTS = ['trew98741.pythonanywhere.com']
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': "trew98741$myblog",
#             'USER': 'trew98741',
#             'PASSWORD': 'a1234567',
#             'HOST': 'trew98741.mysql.pythonanywhere-services.com',
#         }
#     }

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE =  'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 媒体文件地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#用戶上船完成後
# 查看一下项目目录，生成了新的文件夹media/avatar/20181205/，
# 其中存储了该头像文件；查看avatar字段，其保存的是文件的url地址。

CART_SESSION_ID = 'cart'



# Braintree支付網關設置
BRAINTREE_MERCHANT_ID = 'x3d6d35h85tw5my3'  # Merchant ID
BRAINTREE_PUBLIC_KEY = '6g79mmw3sqkfvgjb'  # Public Key
BRAINTREE_PRIVATE_KEY = 'cea662e409990e1b8f4bc7b33042b83c'  # Private key


from braintree import Configuration, Environment

Configuration.configure(
    Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

# Environment.Sandbox,，我們目前是在沙盒環境中操作，
# 不是正式支付環境。如果是在正式支付環境中，必須修改成 Environment.Production。
# 由於我們目前是沙盒測試賬號，這裡的Merchant ID 不是可以用於生產環境的正式ID。

#redis_channel
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [("localhost", 6379)],
#         },
#     },
# }



# redis配置
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100},
#             "PASSWORD": 'a123456',
#         }
#     }
# }
# REDIS_TIMEOUT=7*24*60*60
# CUBES_REDIS_TIMEOUT=60*60
# NEVER_REDIS_TIMEOUT=365*24*60*60