from django.contrib import admin
from . import models
from django.utils.html import format_html
from django.db.models import Count

# customizing the list page
# how we wanna view our Product in admin
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # collection included to show related class Collection
    # as collection __str__ function is set to title, so we will be getting titles instead of Objext addresses, to get id etc still, deifne that method
    list_display  = ['title', 'unit_price', 'inventory_status', 'collection_title']
    # make editable on list page
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection'] # To avoid extra queries

    # Adding computed fields/columns
    @admin.display(ordering='inventory') # used to set meta data properties on the function as if the user clicks this column header, sort the data using the inventory field
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'low'
        return 'Ok'
    
    # method to get collection title or any other field
    def collection_title(self, product):
        return product.collection.title


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10
    list_select_related = ['customer']


    # def customer_name(self, order):
    #     return order.customer.first_name + order.customer.last_name


# or this and admin.site.register(models.Product, ProductAdmin) wcommented  in next lines
# class ProductAdmin(admin.ModelAdmin):
#     list_display  = ['title', 'unit_price']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name'] # we can do ordering here as well instead of meta


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        # return collection.product_count # WHICH DOESNT EXIST SO definging get_queryset(builtin fucntion but we have to customize)
        return format_html('<a href="https://google.com"> {} </a>', collection.product_count)
        # return collection.product_count
        # now we will add a html link whenever we tap on the product_count to jump to the products

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
        )
    # the default query to be returned is added with the annotate method






# Register your models here.

# admin.site.register(models.Collection)
# admin.site.register(models.Product, ProductAdmin)