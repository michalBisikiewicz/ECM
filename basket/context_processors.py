from . basket import MyBasket


def basket(request):
    return {'basket': MyBasket(request)}
