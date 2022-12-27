from django.shortcuts import render
from menu.models import Category, FoodItem
# Create your views here.
from vendor.models import Vendor
from django.db.models import Prefetch
from django.http import HttpResponse, JsonResponse
from menu.models import Category, FoodItem
from .models import Cart


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    vendor_count = vendors.count()
    context = {
        "vendors": vendors,
        "vendor_count": vendor_count,
    }
    return render(request, "marketplace/listing.html", context)


def vendor_detail(request, slug):
    vendor = Vendor.objects.get(vendor_slug=slug)

    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset=FoodItem.objects.filter(is_available=True)
        )
    )

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    context = {
        'vendor': vendor,
        'categories': categories
    }
    return render(request, 'marketplace/vendor_detail.html', context)


def add_to_cart(request, food_id=None):
    if request.user.is_authenticated:
        if is_ajax(request=request):
            try:
                print(food_id)
                fooditem = FoodItem.objects.get(id=food_id)
                try:
                    chkCart = Cart.objects.get(
                        user=request.user, fooditem=fooditem)
                    # increase quantity
                    chkCart.quantity += 1
                    chkCart.save()
                    return JsonResponse({'status': 'failed', 'message': 'increase cart quantity '})
                except:
                    chkCart = Cart.objects.create(
                        user=request.user, fooditem=fooditem, quantity=1)
                    return JsonResponse({'status': 'failed', 'message': ' cart created '})

            except:
                return JsonResponse({'status': 'failed', 'message': 'request is invalid '})

        return JsonResponse({'status': 'success', 'message': 'user is logged in '})
    else:

        return JsonResponse({'status': 'success', 'message': 'please login to continue '})
    return HttpResponse(food_id)


def search(request):
    return HttpResponse('search page')
