from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

from . basket import MyBasket

from store.models import Product
# Create your views here.


def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = MyBasket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        response = JsonResponse({'test': 'data'})
        return response
