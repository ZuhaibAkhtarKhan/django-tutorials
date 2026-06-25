from django.shortcuts import render
# from django.http import HttpResponse
# use request and response of django_framework instead
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view() # so now, the request that goes into product_list will be of rest_framework
def product_list(request):
    return Response('Ok')

@api_view()
def product_detail(request, id):
    return Response(id)