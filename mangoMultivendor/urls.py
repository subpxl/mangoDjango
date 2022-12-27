from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import home
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('vendor/', include('vendor.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('privacy-policy/', TemplateView.as_view(template_name="privacy_policy.html"),
         name='privacy_policy'),
    path('terms/', TemplateView.as_view(template_name="terms.html"), name='terms'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)
