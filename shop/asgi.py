import os
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

django_app = get_asgi_application()

from core import app as fastapi_app

fastapi_app.mount("/django", WSGIMiddleware(django_app))


