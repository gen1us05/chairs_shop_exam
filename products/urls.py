from django.urls import path
from . import views
from .views import ShopPageView, AboutPageView, ServicesPageView, BlogPageView, ContactPageView, CartPageView, ThankyouPageView, ProductDetailView


urlpatterns = [
    path('shop/', ShopPageView.as_view(), name='shop_page'),
    path('aboute/', AboutPageView.as_view(), name='aboute_page'),
    path('service/', ServicesPageView.as_view(), name='service_page'),
    path('blog/', BlogPageView.as_view(), name='blog_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('cart/', CartPageView.as_view(), name='cart_page'),
    path('thankyou/', ThankyouPageView.as_view(), name='thankyou_page'),
    path('products/', ProductDetailView.as_view(), name='products_page'),
]


