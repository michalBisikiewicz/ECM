from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

from . basket import MyBasket

from store.models import Product
# Create your views here.


def basket_summary(request):
    basket = MyBasket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = MyBasket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty': basket_qty})
        return response


def basket_delete(request):
    basket = MyBasket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        print(type(product_id))
        basket.delete(product=product_id)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
