from django.shortcuts import render

# Create your views here.
from vendor.models import Vendor


def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    vendor_count = vendors.count()
    context = {
        "vendors": vendors,
        "vendor_count": vendor_count,
    }
    return render(request, "marketplace/listing.html", context)
