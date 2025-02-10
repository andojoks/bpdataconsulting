"""
URL configuration for bpdataconsulting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from core import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "B&P Data Consulting Admin"
admin.site.site_title = "B&P Data Consulting"
admin.site.index_title = "Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls), # admin site

    path('', views.index, name='index'),          # home page
    path('about/', views.about, name='about'),  # about page
    path('services/', views.services, name='services'),  # services page
    
    
    path('create_contact/',views.create_contact,name='create_contact'),  # new route for POST
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #render static assets

handler404 = views.custom_404_view  # Set the custom 404 view
