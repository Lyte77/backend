from django.urls import path
from .views import ProductListCreateView,ProductRetriveUpdateDestroyView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(),
         name='product-list-create'),
    path('products/<int:pk>/', ProductRetriveUpdateDestroyView.as_view(),
         name='product-detail')
]