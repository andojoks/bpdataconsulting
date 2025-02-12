
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # home page
    path('about/', views.about, name='about'), # about page
    path('services/', views.services, name='services'), # services page
    path('services/<int:service_id>/', views.service_detail, name='service_details'), #service details page
    path('contact_us/', views.contact_us, name='contact_us'), #contact us page
    path('create_contact/',views.create_contact,name='create_contact'), # new route for POST
]