from django.urls import path, include
from .views import vprofile, menu_builder, food_items_by_category, add_category, edit_category, delete_category
from accounts import views as AccountViews


urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', vprofile, name='vprofile'),
    path('menu-builder/', menu_builder, name='menu_builder'),

    # category crud
    path('menu-builder/category/<int:pk>/',
         food_items_by_category, name='food_items_by_category'),
    path('menu-builder/category/add/', add_category, name='add_category'),
    path('menu-builder/category/edit/<int:pk>/',
         edit_category, name='edit_category'),

    path('menu-builder/category/delete/<int:pk>/',
         delete_category, name='delete_category'),

]
