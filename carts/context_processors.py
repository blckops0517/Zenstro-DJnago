from .models import Cart , CartItem
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist

# count function for number of products in cart
# COUNTER COME FROM THIS CONTEXT PROCESSOR

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:                                   # IF THE USER IS LOGIN THAT CART ITEM ASIGNED TO THAT USER
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items =CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count +=cart_item.quantity
        except Cart.ObjectDoesNotExist:         # Cart.ObjectDoesNotExist: THIS LINE ACTUALY Cart.DoesNotExists:
            cart_count = 0
    return dict(cart_count=cart_count)