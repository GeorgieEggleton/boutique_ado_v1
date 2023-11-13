from django.shortcuts import render

def view_bag(request):
    """ A view to return the bag contents """

    return render(request, 'bag/bag.html')
