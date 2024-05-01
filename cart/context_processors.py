from .models import CartItem
from .views import _cart_id

def counter(request):
    if 'admin' in request.path:
        return {}  # Do not count items in the cart for admin pages
    else:
        try:
            cart = CartItem.objects.get(cart_id=_cart_id(request)).cart
            item_count = CartItem.objects.filter(cart=cart).count()
        except CartItem.DoesNotExist:
            item_count = 0
    return {'item_count': item_count}
