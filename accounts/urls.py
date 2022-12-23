from django.urls import path, include
from .views import registerUser, registerVendor, login, logout, myAccount, vendorDashboard, customerDashboard

urlpatterns = [
    path('registerUser/', registerUser, name='registerUser'),
    path('registerVendor/', registerVendor, name='registerVendor'),
    path('customerDashboard/', customerDashboard, name='customerDashboard'),
    path('vendorDashboard/', vendorDashboard, name='vendorDashboard'),
    path('vendor/', include('vendor.urls')),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('myAccount/', myAccount, name='myAccount'),

]
