from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat

# querying generic relations
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
# Product already imported

def say_hello(request):

    # try:

    #     # product = null, no exception at all
    #     exists = Product.objects.filter(pk = 0).exists() # We get a query, that is evaluated later
    # # count() function do not return a query set, it returns a number (count), and there are other functions(eg get()) as well, that do nmot return a query set
    # except ObjectDoesNotExist:
    #     pass

    # queryset api (field lookups) cuz unit_price > 20 returns boolean which filter do not expect 
    # queryset = Product.objects.filter(last_update__year = 2021)

    # q1 = Customer.objects.filter(email__icontains='.com')

    # q2 = Collection.objects.filter(featured_product__isnull = True)

    # q3 = Product.objects.filter(inventory__lt = 10)

    # q4 = Order.objects.filter(customer__id = 1)

    # q5 = OrderItem.objects.filter(product__collection__id=3)

    # Product: inventory < 10 AND price < 20

    # queryset = Product.objects.filter(inventory__lt = 10, unit_price__lt = 20)
    # queryset = Product.objects.filter(inventory__lt = 10).filter(unit_price__lt = 20)

    # Product: inventory < 10 OR price < 20 (Q objects)
    # queryset = Product.objects.filter(Q(inventory__lt = 10) | ~Q(unit_price__lt = 20))

    # comparing two fields (F Objects)
    # queryset = Product.objects.filter(inventory = F('collection__id'))

    #Sorting

    # queryset = Product.objects.order_by('unit_price','-title').reverse()

    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price') # sort the result by unit price in ASC and get the first object
    # product = Product.objects.latest('unit_price') # sort the result by unit price in DSC and get the first object


    # LIMITING RESULTS
    # queryset = Product.objects.all()[5:10]

    # SELECTING FIELDS TO QUERY
    # queryset = Product.objects.values_list('id', 'title', 'collection__title') # values gives dicts and values_list gives tuples

    
    # queryset = Product.objects.filter(id__in =OrderItem.objects.values('product_id').distinct()).order_by('title')

    # queryset = OrderItem.objects.values('product__title').distinct().order_by('product__title') # Just had to chnage the html


    # DERERRING FIELDS
    # queryset = Product.objects.only('id', 'title')
    # only returns the object instsances while values return dictionaries
    # only make objects, so if a non-existing parameter is typed in it, for each object, it will run a sql query trying to fetch that non-existing parameter

    # defer is the opposite of only
    # queryset = Product.objects.defer('description')

    # SELECTING RELATED OBJECTS
    # queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.select_related('collection__someOtherField').all()
    # select_related is kinda join in sql, so that there wouldn't be a second derived query and works for 1 to many (not many to one (Reverse foreign key))

    # for many to one, many to many and reverse foreign key, we got prefetch_related
    # queryset = Product.objects.prefetch_related('promotions').all()

    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]


    # aggregate

    # result = Product.objects.filter(collection__id=1).aggregate(count = Count('id'), min_price = Min('unit_price'))

    # result = Order.objects.aggregate(count = Count('id'))

    # result = OrderItem.objects.filter(product__id = 1).aggregate(count = Sum('quantity'))

    # result = Order.objects.filter(customer__id = 1).aggregate(count = Count('id'))


    # queryset = Customer.objects.annotate(is_new=Value(True))
    # if there isnt Value() then the django willl search for Column True, which it wouldnt find to rename throwing an error. Now as it is as Value, True is filled in every column named is_new

    # queryset = Customer.objects.annotate(is_new=F('id'))

    # we can perform computations as well.

    # queryset = Customer.objects.annotate(is_new=F('id')+1)


    # queryset = Customer.objects.annotate(
    #     # CONCAT
    #     full_name = Func(F('first_name'),Value(' '), F('last_name'), function='CONCAT')
    # )

    # another method is to use concat function from django, we have to import it first


    # queryset = Customer.objects.annotate(
    #     # CONCAT USING DjNAGO FUNCTION
    #     full_name = Concat('first_name',Value(' '), 'last_name')
    #     # BENEFIT IS THAT WE DO NOT hAVE TO RAP IT IN AN F OBJECT BUt FOR A WHITE SPACE WE HAVE T WRAP IT INSIDE A VALUE OBJECT
    # )

    #GROUPING

    # queryset = Customer.objects.annotate(
    #     orders_count = Count('order')
    # )

    # EXPRESSION WRAPPER

    # queryset = Product.objects.annotate(
    #     discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # )


    # Content Types (Generic relations)

    # Get for model gives the content_object_id for the class in it 
    # content_type = ContentType.objects.get_for_model(Product)

    # queryset = TaggedItem.objects.select_related('tag').filter(
    #     content_type = content_type,
    #     object_id = 1
    # )

    # Custom methods
    # Go to models.py where you wanna create
    # created get_tag_for there

    queryset = TaggedItem.objects.get_tags_for(Product, 1)


    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})
