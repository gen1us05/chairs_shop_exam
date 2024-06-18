from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
django_app = get_asgi_application()

app = FastAPI()

# Mount the Django app
app.mount("/django", WSGIMiddleware(django_app))


# Import and include the product router
from api.product_api import router as product_router
from api.blog_api import router as blog_router

app.include_router(product_router, prefix="/api")
app.include_router(blog_router, prefix="/api")
