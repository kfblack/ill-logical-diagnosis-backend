import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ill_logical_diagnosis_backend.settings')

application = get_wsgi_application()
