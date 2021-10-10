from django.shortcuts import render
import json

# Create your views here.
def products(request):
    title = 'Каталог'
    with open ('mainapp/products_list.json', 'r') as f:
        links_menu = json.load(f)

    context = {'title': title, 'links_menu': links_menu}
    return render(request, 'mainapp/products.html', context)