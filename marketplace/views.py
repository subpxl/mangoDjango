from django.shortcuts import render
from vendor.models import Vendor
from menu.models import Product, Category


def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    vendor_count = vendors.count()
    context = {
        "vendors": vendors,
        "vendor_count": vendor_count,
    }
    return render(request, "seller_list.html", context)


def seller_details(request, slug):
    vendor = Vendor.objects.get(vendor_slug=slug)
    categories = Category.objects.filter(vendor=vendor)
    products = Product.objects.filter(vendor=vendor)
    product_count = products.count()
    deals = Product.objects.filter(vendor=vendor)

    context = {
        "vendor": vendor,
        "products": products,
        "categories": categories,
        "deals": deals,
        "product_count": product_count
    }
    return render(request, 'seller.html', context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'category_list.html', context)


def product_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'product_by_categories.html', context)
