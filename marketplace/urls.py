from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.product_by_category,
         name='product_by_category'),
    path('', views.marketplace, name='marketplace'),
    path('seller/<slug:slug>/', views.seller_details, name='seller_details'),
]
