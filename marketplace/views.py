from django.shortcuts import render, redirect
from vendor.models import Vendor
from menu.models import Product, Category
from django.db.models import Q
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')
    else:
        form = ContactForm()
        context = {
            "form": form
        }
    return render(request, 'contact.html', context)


def cart(request):
    return render(request, "cart.html", )


def wishlist(request):
    return render(request, "wishlist.html", )


def deals(request):
    return render(request, "deals.html", )


def checkout(request):
    return render(request, "checkout.html", )


def sellers(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    vendor_count = vendors.count()
    context = {
        "vendors": vendors,
        "vendor_count": vendor_count,
    }
    return render(request, "seller_list.html", context)


def search(request):
    if request.method == "POST":
        products = Product.objects.all()
        vendors = Vendor.objects.all()
        product_count = products.count()
        vendor_count = vendors.count()
        context = {
            "products": products,
            "vendors": vendors,
            "product_count": product_count,
            "vendor_count": vendor_count,

        }
        return render(request, "result.html", context)


def marketplace(request):
    products = Product.objects.filter()
    product_count = products.count()
    context = {
        "products": products,
        "product_count": product_count,
    }
    return render(request, "product_by_categories.html", context)


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
    category_count = categories.count()

    context = {
        "category_count": category_count,
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
