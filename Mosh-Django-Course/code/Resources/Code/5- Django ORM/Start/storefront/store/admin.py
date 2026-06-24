from django.contrib import admin
from . import models
from django.utils.html import format_html, urlencode
from django.db.models import Count
from django.urls import reverse


# class InventoryFilter(admin.SimpleListFilter):
#     title = 'Inventory'
#     parameter_name = 'inventory' 

#     def lookups(self, request, model_admin):
#         return [
#             ('<10', 'low')
#         ]

#     def queryset(self, request, queryset):
#         if self.value() == '<10':
#             return queryset.filter(inventory__lt=10)

class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'low')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


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

    # adding filters # adding custom filter (making InventoryFilter class)
    list_filter=['collection', 'last_update', InventoryFilter]

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


# @admin.register(models.Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'membership', 'order_count']
#     list_editable = ['membership']
#     list_per_page = 10
#     ordering = ['first_name', 'last_name'] # we can do ordering here as well instead of meta


#     @admin.display(ordering='order_count')
#     def order_count(self, customer):
#         url = (reverse('admin:store_order_changelist') + '?' + urlencode({
#             'customer__id':str(customer.id)
#         }))
#         return format_html('<a href="{}">{}</a>', url, customer.order_count)
    
#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(
#             order_count = Count('order')
#         )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'order_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering=['first_name', 'last_name']
    search_fields=['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='order_count')
    def order_count(self, customer):

        # return customer.order_count
        url = (reverse('admin:store_order_changelist') + '?' + urlencode({
            'customer__id': str(customer.id)
        }))
        return format_html('<a href="{}" >{}</a>', url, customer.order_count )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count = Count('order')
        )
    


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        # return collection.product_count # WHICH DOESNT EXIST SO definging get_queryset(builtin fucntion but we have to customize)
        # reverse('admin:app_model_page')
        url = (reverse('admin:store_product_changelist') + '?' + urlencode({
            'collection__id': str(collection.id)
        }))
        return format_html('<a href="{}"> {} </a>',url, collection.product_count)
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