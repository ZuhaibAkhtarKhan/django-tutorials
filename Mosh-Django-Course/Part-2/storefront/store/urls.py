from django.urls import path
from .import views

urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductList.as_view()),
    # path('products/<int:id>/', views.product_detail),
    path('products/<int:pk>/', views.ProductDetails.as_view()),
    path('collections/', views.CollectionList.as_view()),
    # path('collections/<int:pk>/', views.collection_detail, name='collection-detail')
    path('collections/<int:pk>/', views.CollectionDetails.as_view(), name='collection-detail')
]