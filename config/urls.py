"""config URL Configuration

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
from core import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "B&P Data Consulting Admin"
admin.site.site_title = "B&P Data Consulting"
admin.site.index_title = "Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls), # admin site
    path('', include('core.urls')),  # Include the core app's URLs
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #render static assets

handler404 = views.custom_404_view  # Set the custom 404 view
