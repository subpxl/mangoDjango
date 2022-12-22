from django.shortcuts import redirect, render,get_object_or_404
from accounts.forms import UserProfileForm
from .forms import VendorForm
# Create your views here.
from .models import Vendor
from vendor.models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from accounts.views import check_role_vendor
from menu.models import Category,FoodItem
from menu.forms import CategoryForm
from django.template.defaultfilters import slugify



def get_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    return vendor


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vprofile(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    vendor = get_object_or_404(Vendor,user=request.user)
    
    if request.method=="POST":
        profile_form =UserProfile(request.POST,request.FILES,instance=profile)
        vendor_form = VendorForm(request.POST,request.FILES,instance=profile)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request,'settings updated successfully')
        else:
            print(profile_form.errors)
            print(vendor_form.errors)

    profile_form = UserProfileForm(instance=profile)
    vendor_form = VendorForm(instance=vendor)
    context ={
        'profile_form':profile_form,
        'vendor_form':vendor_form,
        'profile':profile
    }
    return render(request,'vendor/vprofile.html',context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menu_builder(request):
    vendor = get_vendor(request)
    print('vendor is ',vendor)
    categories = Category.objects.filter(vendor=vendor)
    # categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'vendor/menu_builder.html',context)

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def food_items_by_category(request,pk=None):
    # vendor = Vendor.objects.get(user=request.user)
    vendor = get_vendor(request)
    category = get_object_or_404(Category,pk=pk)
    fooditems = FoodItem.objects.filter(vendor=vendor,category=category)
    context = {
        'fooditems':fooditems,
        'category':category,
    }
    return render(request, 'vendor/fooditems_by_category.html',context )


def add_category(request):

    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category= form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug=slugify(category.name)
            form.save()
            messages.success(request, 'category created')
            return redirect("menu_builder")
    else:
        form = CategoryForm()
    context= {
        'form':form
    }    
    return render(request, 'vendor/add_category.html',context)