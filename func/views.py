from urllib import request

from django.template import RequestContext
from django.shortcuts import render_to_response, render


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'hsp/index.html')
def products(request):
    return render(request, 'hsp/products.html')
def brands(request):
    return render(request, 'hsp/brands.html')
def about(request):
    return render(request, 'hsp/base.html')
def login(request):
    return render(request, 'hsp/login.html')
def order(request):
    return render(request, 'hsp/order.html')
def home(request):
    return render(request, 'hsp/index.html')