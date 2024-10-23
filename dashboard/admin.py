from django.contrib import admin
from .models import Product ,Order  #to pull data into db

#how to unregister a model
from django.contrib.auth.models import Group


# Register your models here.

#to change admin title
admin.site.site_header = 'Inventory System'

class ProductAdmin(admin.ModelAdmin): #display list from db in table form incase you see objects
	list_display = ('name','category','quantity')
	#list_filter = ('category',)
	
admin.site.register(Product,ProductAdmin)
#admin.site.unregister(Group)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff', 'order_quantity')

admin.site.register(Order,OrderAdmin)

