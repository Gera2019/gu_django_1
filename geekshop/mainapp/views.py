from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductsCategory, Product
from basketapp.models import Basket

# Create your views here.

def products(request, pk=None):
    title = 'Каталог'
    links_menu = ProductsCategory.objects.all()
    products = Product.objects.order_by('price')
    basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductsCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context )

    same_products = Product.objects.all()[1:2]

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context)
