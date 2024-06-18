from django.shortcuts import render
from django.views import View
from products.models import Product, Blog


class ShopPageView(View):

    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }

        return render(request, 'main/shop.html', context)

class AboutPageView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class ServicesPageView(View):
    def get(self, request):
        return render(request, 'main/services.html')


class BlogPageView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        contex = {
            'blogs': blogs
        }
        return render(request, 'main/blog.html', contex)


class ContactPageView(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class CartPageView(View):
    def get(self, request):
        return render(request, 'main/cart.html')


class ThankyouPageView(View):
    def get(self, request):
        return render(request, 'main/thankyou.html')



class ProductDetailView(View):
    def get(self, request):
        return render(request, 'main/product.html')

