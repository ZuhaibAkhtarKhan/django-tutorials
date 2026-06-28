from django.urls import path
# from rest_framework.routers import SimpleRouter
# there is that DefaultRouter as well with 2 not so important extra features

# now making nested routers
from rest_framework_nested import routers
from .import views


# router = DefaultRouter() # This is when we use routers from rest_framework.routers but for nested_rest we use
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls

# urlpatterns = [
# #     # path('products/', views.product_list),
# #     path('products/', views.ProductList.as_view()),
# #     # path('products/<int:id>/', views.product_detail),
# #     path('products/<int:pk>/', views.ProductDetails.as_view()),
# #     path('collections/', views.CollectionList.as_view()),
# #     # path('collections/<int:pk>/', views.collection_detail, name='collection-detail')
# #     path('collections/<int:pk>/', views.CollectionDetails.as_view(), name='collection-detail')
# ]

