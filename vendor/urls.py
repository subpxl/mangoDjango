from django.urls import path,include
from .views import vprofile,menu_builder,food_items_by_category,add_category
from accounts import views as AccountViews


urlpatterns = [
    path('',AccountViews.vendorDashboard,name='vendor'),
    path('profile/',vprofile,name='vprofile'),
    path('menu-builder/',menu_builder,name='menu_builder'),
    path('menu-builder/category/<int:pk>/',food_items_by_category,name='food_items_by_category'),
 
    # category crud
    path('menu-builder/category/add/',add_category,name='add_category'),

]