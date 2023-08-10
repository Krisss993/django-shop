from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import core.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('accounts/', include('allauth.urls')),
    path('staff/', include('staff.urls', namespace='staff')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
