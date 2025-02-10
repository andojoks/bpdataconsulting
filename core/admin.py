from django.contrib import admin
from .models import Service, Contact, Product, Client, Subscription

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price', 'status', 'date_included', 'on_promotion', 'discount')
    search_fields = ('service_name', 'description')
    list_filter = ('status', 'on_promotion')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'subject', 'email', 'contact_date')
    search_fields = ('fname', 'lname', 'email', 'subject','contact_date')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'created', 'updated')
    search_fields = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'is_active', 'country')
    search_fields = ('email', 'fname', 'lname')
    list_filter = ('is_active', 'country')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('product', 'client', 'status', 'start_date', 'end_date')
    search_fields = ('product__name', 'client__email')
    list_filter = ('status', 'start_date', 'end_date')

