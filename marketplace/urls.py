from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),

    path('category/<slug:slug>/', views.product_by_category,
         name='product_by_category'),
    path('sellers/', views.sellers, name='sellers'),
    path('seller/<slug:slug>/', views.seller_details, name='seller_details'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),

    path('deals/', views.deals, name='deals'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.marketplace, name='marketplace'),
]
