from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products')) #Prevents people from manually accessing the URL by typing /checkout

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key' : 'pk_test_51OFgV1HNBgyzsvZ1qRisfwGEnGbMjo5DsdHGL3DgaVFZ8DISR7jUmuR3NwJxg9vjymJpdcejvHXAzvpVggxgHhHI00X7FF4L5H',
        'client_secret' : 'test client secret'
    }

    return render(request, template, context)
