from django.urls import path,include
from .views import registerUser,registerVendor,login,logout,myAccount,vendorDashboard,customerDashboard

urlpatterns = [
    path('',myAccount,name='myAccount'),
    path('registerUser/',registerUser,name='registerUser'),
    path('registerVendor/',registerVendor,name='registerVendor'),

    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('customerDashboard/',customerDashboard,name='customerDashboard'),
    path('vendorDashboard/',vendorDashboard,name='vendorDashboard'),


    path('vendor/',include('vendor.urls')),

]