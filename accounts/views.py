from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from django.contrib import messages
# Create your views here.

def registerUser(request):
    if request.method=="POST":
        print(request.POST)
        form=UserForm(request.POST)
        if form.is_valid():
            # create use using form
            password=form.changed_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role=User.CUSTOMER
            form.save()

            # create user using create_user method
            first_name= form.changed_data['first_name']
            last_name= form.changed_data['last_name']
            username= form.changed_data['username']
            email= form.changed_data['email']
            password= form.changed_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            print('user is created')
            messages.success(request, 'your account has been regusters successfully')
            return redirect('registerUser')
    else:
        form = UserForm()
    context = {
        'form':form
    }
    return render(request, 'registerUser.html',context)
    