from django.shortcuts import render
from basketapp.models import Basket
from mainapp.models import Product
from contactsapp.models import Contact

def main(request):
    title = 'Магазин'

    basket = Basket.objects.filter(user=request.user)
    products = Product.objects.all()
    contacts = Contact.objects.all()


    context = {
        'title': title,
        'products': products,
        'contacts': contacts,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context)

