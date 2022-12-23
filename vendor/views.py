from django.shortcuts import redirect, render, get_object_or_404
from accounts.forms import UserProfileForm
from .forms import VendorForm
# Create your views here.
from .models import Vendor
from vendor.models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.views import check_role_vendor
from menu.models import Category, FoodItem
from menu.forms import CategoryForm, FoodItemForm
from django.template.defaultfilters import slugify

from django.http import HttpResponse


def get_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    print('get_vendor ', vendor)
    return vendor


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == "POST":
        profile_form = UserProfile(
            request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'settings updated successfully')
        else:
            print(profile_form.errors)
            print(vendor_form.errors)

    profile_form = UserProfileForm(instance=profile)
    vendor_form = VendorForm(instance=vendor)
    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile': profile
    }
    return render(request, 'vendor/vprofile.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menu_builder(request):
    vendor = get_vendor(request)
    print('vendor is ', vendor)
    categories = Category.objects.filter(vendor=vendor).order_by('-created_at')
    # categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'vendor/menu_builder.html', context)


# category crud
@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def food_items_by_category(request, pk=None):
    # vendor = Vendor.objects.get(user=request.user)
    vendor = get_vendor(request)
    category = get_object_or_404(Category, pk=pk)
    fooditems = FoodItem.objects.filter(vendor=vendor, category=category)
    context = {
        'fooditems': fooditems,
        'category': category,
    }
    return render(request, 'vendor/fooditems_by_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def add_category(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category.category_name)
            form.save()
            messages.success(request, 'category created')
            return redirect("menu_builder")
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'vendor/add_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def edit_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category.category_name)
            form.save()
            messages.success(request, 'category created')
            return redirect("menu_builder")
    else:
        form = CategoryForm(instance=category)
    context = {
        'category': category,
        'form': form
    }
    return render(request, 'vendor/edit_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def delete_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'category deleted successfully')
    return redirect('menu_builder')


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def add_food(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():

            foodtitle = form.cleaned_data['food_title']
            food = form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(foodtitle)
            form.save()
            messages.success(request, 'food item  created')
            return redirect("food_items_by_category", food.category.id)
        else:
            print(form.errors)
    else:

        form = FoodItemForm()
        # get category only of vendor
        form.fields['category'].queryset = Category.objects.filter(
            vendor=get_vendor(request))
    context = {
        "form": form
    }

    return render(request, 'vendor/add_food.html', context)


def edit_food(request, pk=None):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            foodtitle = form.cleaned_data['food_title']
            food = form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(foodtitle)
            form.save()
            messages.success(request, 'fooditem edited successfully')
            return redirect("food_items_by_category", food.category.id)
    else:
        form = FoodItemForm(instance=food)
        # get category only of vendor
        form.fields['category'].queryset = Category.objects.filter(
            vendor=get_vendor(request))
    context = {
        'food': food,
        'form': form
    }
    return render(request, 'vendor/edit_food.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def delete_food(request, pk=None):
    food = get_object_or_404(FoodItem, pk=pk)
    food.delete()
    messages.success(request, 'food deleted successfully')
    return redirect('menu_builder')
