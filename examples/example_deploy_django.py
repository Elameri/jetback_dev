import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from django.urls import path
from django.http import JsonResponse
from jetback_dev import jetback_deploy_django

# Configure Django settings
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
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
        ],
        DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
    )

# Define your Django view
def hello(request):
    return JsonResponse({"message": "Hello from Django on JetBack.Dev :D !"})

# Define URL patterns
urlpatterns = [
    path('', hello, name='hello'),
]

# Get the WSGI application
django_app = get_wsgi_application()

# Deploy the Django app
jetback_deploy_django(django_app)

