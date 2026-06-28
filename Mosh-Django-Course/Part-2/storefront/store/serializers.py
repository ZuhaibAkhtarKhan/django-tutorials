from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection, Review

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
    products_count = serializers.IntegerField(read_only=True)

# serializers converts models to dict and then dict will be converted to JSON by render fucntion
class ProductSerializer(serializers.ModelSerializer):
    # INstead JUST DO THE BELOW AFYTER THIS
        # id = serializers.IntegerField()
        # title = serializers.CharField(max_length=255)
        # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
        # # price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    #
    class Meta:
        model = Product
        fields = ['id', 'title','description','slug', 'inventory', 'unit_price', 'collection','price_with_tax' ]
        # fields = '__all__' but bad practice, cuz sensitive info may be exposed


    
    #
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # if we wanna return the collection as a string instead of a digit
    # collection = serializers.StringRelatedField() # extra queriessss!!!  # so we do select_related in views.py

    # now lets put a collection object instaed of string
    #define class CollectionSerializer
    # collection = CollectionSerializer() # Lets make hyperlinks next

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(), 
    #     view_name='collection-detail'
    # )

    # Overwrirting can be done if Meta subclass
    # collection = serializers.HyperlinkedRelatedField (
    #     queryset = Collection.objects.all(),
    #     view_name = 'collection-detail'
    # )

    def calculate_tax(self, product):
        return (product.unit_price) * Decimal(1.1)
    
    # overriding teh validator method of serializer
    # just an example
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match')
    #     return data



    # customizing how a product is created (overriding create method)
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1 # customizing any other field in it
    #     product.save()
    #     return product
    
    # def update(self, instance, validated_data): # instance -> product object
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','product', 'name', 'description', 'date']