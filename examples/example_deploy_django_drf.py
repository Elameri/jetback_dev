import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from django.urls import path
from jetback_dev import jetback_deploy_django

# Configure Django settings
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from django.conf import settings
    settings.configure(
        DEBUG=True,
        SECRET_KEY='your-secret-key',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],  # Allow all hosts.
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'rest_framework',
        ],
        REST_FRAMEWORK={
            'DEFAULT_RENDERER_CLASSES': [
                'rest_framework.renderers.JSONRenderer',
            ],
            'DEFAULT_PARSER_CLASSES': [
                'rest_framework.parsers.JSONParser',
            ],
        },
        DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
    )

# Now that settings are configured, we can import DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Define your Django REST Framework view
@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Django REST Framework on JetBack.Dev :D !"})

# Define URL patterns
urlpatterns = [
    path('', hello, name='hello'),
]

# Get the WSGI application
django_app = get_wsgi_application()

# Deploy the Django app
jetback_deploy_django(django_app)


"""
django>=3.2,<6.0
djangorestframework==3.12.*
"""