from django.shortcuts import render
from mainapp.models import Product
from contactsapp.models import Contact

def main(request):
    title = 'Магазин'

    products = Product.objects.all()
    contacts = Contact.objects.all()
    # slider = Slider.object.all()

    context = {
        'title': title,
        'products': products,
        'contacts': contacts,
    }
    return render(request, 'geekshop/index.html', context)

