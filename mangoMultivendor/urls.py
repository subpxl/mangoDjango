from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from marketplace import views as marketplaceViews

from .views import home
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('vendor/', include('vendor.urls')),
    path('marketplace/', include('marketplace.urls')),

    path('search/', marketplaceViews.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
