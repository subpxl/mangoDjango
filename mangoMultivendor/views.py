from django.shortcuts import render
from vendor.models import Vendor


def home(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    # vendors = Vendor.objects.all()
    categories = ['a', 'a', 'a', 'a', 'a', 'a', 'a', ]
    print(vendors)
    context = {
        "vendors": vendors,
        "categories": categories
    }
    return render(request, 'index.html', context)
