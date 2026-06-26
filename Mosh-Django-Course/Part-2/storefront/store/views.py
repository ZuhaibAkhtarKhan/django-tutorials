from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# use request and response of django_framework instead
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

@api_view() # so now, the request that goes into product_list will be of rest_framework
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many=True, context={'request':request}) # many = True so that serilizer loop over through query set
    return Response(serializer.data)



@api_view()
def product_detail(request, id):
    # try:
        # product = Product.objects.get(pk=id)
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    # except Product.DoesNotExist:
    #     # return Response(status=404)
    #     return Response(status=status.HTTP_404_NOT_FOUND)

@api_view()
def collection_detail(request, pk):
      return Response('ok')