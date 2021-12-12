# -*- encoding: utf-8 -*-
"""subul_al_khayrat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.app import views
# APPs importation



urlpatterns = [
    path("", views.Index_View.as_view(), name='home'),
    path('admin/', admin.site.urls, name='admin'),          # Django admin route
    path("app/", include("apps.app.urls", namespace="app")),
    # Auth routes - login / register
    path("", include("apps.authentication.urls", namespace='account')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0,path('__debug__/', include(debug_toolbar.urls)))
 
  

