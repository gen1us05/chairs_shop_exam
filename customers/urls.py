from django.urls import path
from .views import LandingPageView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
