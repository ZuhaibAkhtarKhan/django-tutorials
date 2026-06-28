from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# use request and response of django_framework instead
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Collection, OrderItem, Review
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from django.db.models import Count

# Class based views
# class ProductList(APIView):
#     # we will define get and post request
#     def get(self, request):
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(queryset, many=True, context={'request':request}) # many = True so that serilizer loop over through query set
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status = status.HTTP_201_CREATED)
    

# lets use generics for the above
# class ProductList(ListCreateAPIView):
#     # just override queryset and serilizer class and context fro some
#     # def get_queryset(self):
#     #     return Product.objects.select_related('collection').all()

#     # or if we do not need much customization then queryset as:

#     # queryset = Product.objects.select_related('collection').all()
#     queryset = Product.objects.all()
    
#     # def get_serializer_class(self):
#     #     return ProductSerializer # just teh class, not product

#     # or

#     serializer_class = ProductSerializer
    
#     def get_serializer_context(self):
#         return {'request':self.request}



# class ProductDetails(APIView):
#     # product = get_object_or_404(Product, pk=id)

#     def get(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     def put(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because its associated with a OrderItem'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     # if we must have id, not pk in our url then use lookup
#     # lookup_field = 'id'

#     # in our delete function we had that error: description thing, so we can override delete

#     def delete(self, request, pk):
#         product = get_object_or_404(Product, id=pk)
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because its associated with a OrderItem'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.

# function based views, but we can make class based views as as

# @api_view(['GET', 'POST']) # so now, the request that goes into product_list will be of rest_framework
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(queryset, many=True, context={'request':request}) # many = True so that serilizer loop over through query set
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # deseliarization
#         serializer = ProductSerializer(data=request.data)
#         # serializer.validated_data
#         # but first lets validate the data
#         # if serializer.is_valid():
#         #     serializer.validated_data
#         #     return Response('OK')
#         # else:
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # get rid of the if-else statement by raise_exception=True
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(serializer.validated_data)
#         return Response(serializer.data, status = status.HTTP_201_CREATED)




# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, id):
#     # try:
#         # product = Product.objects.get(pk=id)

#     product = get_object_or_404(Product, pk=id)

#     if request.method  == 'GET':
#         # product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     # except Product.DoesNotExist:
#     #     # return Response(status=404)
#     #     return Response(status=status.HTTP_404_NOT_FOUND)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because its associated with a OrderItem'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         queryset= Collection.objects.all()
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.annotate(
#         products_count = Count('products')
#     ).all()
#     serializer_class = CollectionSerializer

#     def get_serializer_context(self):
#         return {'request':self.request}


# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection = get_object_or_404(Collection, pk = pk)
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializer(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error': 'Cannot delete the collection as it is associated with other products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class CollectionDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer
    
#     def delete(self, request, pk):
#         collection = get_object_or_404(Collection, id = pk)
#         if collection.products.count() > 0:
#             return Response({'error': 'Cannot delete the collection as it is associated with other products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# lets lessen the code even more
# but for them, we will have to make routers in urls.py
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}
    
    # for this ViewSet setting, delete is actually destroy internally, so we shoudl override destroy

    # def delete(self, request, pk):
    #     product = get_object_or_404(Product, id=pk)
    #     if product.orderitems.count() > 0:
    #         return Response({'error': 'Product cannot be deleted because its associated with a OrderItem'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id = kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted because its associated with a OrderItem'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
# we also have just ReadOnlyModelViewSet to just enable read only operations
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {'request':self.request}
    
    # def delete(self, request, pk):
    #     collection = get_object_or_404(Collection, id = pk)
    #     if collection.products.count() > 0:
    #         return Response({'error': 'Cannot delete the collection as it is associated with other products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id= kwargs['pk']).count() > 0:
            return Response({'error': 'Cannot delete the collection as it is associated with other products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer