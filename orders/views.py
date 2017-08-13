from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from .models import Order

product_list = [ 'Gin Tonic', 'Cola Rum',
                'Vodka Orange', 'Vodka Bull']
# 'Mojito', 'Caipirinha'
# , 'Vodka Makava'
context = {
    'product_list': product_list
}

def index(request):
    return render(request, 'orders/index.html', context)


def orderList(request):

    c = {'orders': Order.objects.order_by('-submitted_date')}
    return render(request, 'orders/list.html', c)

# ...
def select(request):
    print('########################')
    # order = get_object_or_404(Order)
    try:
        drink=request.POST['choice']
        print(drink)

        name = request.POST['name']
        print(name)

        wishes = request.POST['wishes']

        print(drink + wishes + name)

        o = Order(name= name, drink = drink, extra = wishes, ready=False, submitted_date=datetime.datetime.now())
        o.save()
    except (KeyError, Order.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'orders/index.html', {
            'product_list': product_list,
            'error_message': "You didn't select a choice.",
        })
    else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
        return render(request, 'orders/ordered.html', {'choice': drink})