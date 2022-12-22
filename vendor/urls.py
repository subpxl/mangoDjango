from django.urls import path,include
from .views import vprofile,menu_builder,food_items_by_category
from accounts import views as AccountViews


urlpatterns = [
    path('',AccountViews.vendorDashboard,name='vendor'),
    path('profile/',vprofile,name='vprofile'),
    path('menu-builder/',menu_builder,name='menu_builder'),
    path('menu-builder/category/<int:pk>/',food_items_by_category,name='food_items_by_category'),
 
]