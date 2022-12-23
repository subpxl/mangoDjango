from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages, auth

# Create your views here.
from vendor.forms import VendorForm
from .utils import detectUser
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

# restrict customer from entering vendor


def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        return PermissionDenied
# restrict vendor from entering customer


def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        return PermissionDenied


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already loggedin')
        return redirect('myAccount')
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # create use using form
            # password=form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # form.save()

            # create user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            print('user is created')
            messages.success(
                request, 'your account has been regusters successfully')
            return redirect('myAccount')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/registerUser.html', context)


def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already loggedin')
        return redirect('myAccount')
    elif request.method == "POST":
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)

        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user.pk)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(
                request, 'your account has been registered, please wait for approval')
            return redirect('login')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        v_form = VendorForm()
    context = {
        'form': form,
        'v_form': v_form
    }
    return render(request, 'accounts/registerVendor.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already loggedin')
        return redirect('myAccount')

    elif request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now loggedin')
            return redirect('myAccount')
            # return redirect('vprofile')

        else:
            messages.error(request, 'invalid credenteials')
            return redirect('login')
    context = {
        "": ""
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    messages.info(request, 'you are logged out')
    return redirect('login')


@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    print('user type is ', redirectUrl)
    return redirect(redirectUrl)


@login_required(login_url='login')
# @user_passes_test(check_role_vendor)
def vendorDashboard(request):
    return render(request, 'accounts/vendorDashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def customerDashboard(request):
    return render(request, 'accounts/customerDashboard.html')
