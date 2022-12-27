# mango
 generic marketplace django


<!-- auth urls -->
path('registerUser/', registerUser, name='registerUser'),
path('registerVendor/', registerVendor, name='registerVendor'),
path('customerDashboard/', customerDashboard, name='customerDashboard'),
path('vendorDashboard/', vendorDashboard, name='vendorDashboard'),
path('login/', login, name='login'),
path('logout/', logout, name='logout'),
path('myAccount/', myAccount, name='myAccount'),


<!-- base apps -->
path('', home, name='home'),
path('admin/', admin.site.urls),
path('', include('accounts.urls')),
path('vendor/', include('vendor.urls')),
path('marketplace/', include('marketplace.urls')),



<!-- marketplace app -->
# seller frontend
path('', views.marketplace, name='marketplace'),
path('<slug:slug>/', views.seller_details, name='seller_details'),



<!-- menu app -->
no urls

# seller backend
# vendor app

path('', AccountViews.vendorDashboard, name='vendor'),
path('profile/', vprofile, name='vprofile'),
path('menu-builder/', menu_builder, name='menu_builder'),


# food crud
path('menu-builder/food/add/', add_food, name='add_food'),
path('menu-builder/food/edit/<int:pk>/',
     edit_food, name='edit_food'),

path('menu-builder/food/delete/<int:pk>/',
     delete_food, name='delete_food'),

# category crud
path('menu-builder/category/<int:pk>/',
     food_items_by_category, name='food_items_by_category'),
path('menu-builder/category/add/', add_category, name='add_category'),
path('menu-builder/category/edit/<int:pk>/',
     edit_category, name='edit_category'),

path('menu-builder/category/delete/<int:pk>/',
     delete_category, name='delete_category'),
