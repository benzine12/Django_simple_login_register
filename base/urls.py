from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', views.index),
    path('products/', views.get_all_products, name='get_all_products'),  # List all products
    path('products/create/', views.create_product, name='create_product'),  # Create a new product
    path('products/<int:pk>/', views.get_product, name='get_product'),  # Get a single product
    path('products/<int:pk>/update/', views.update_product, name='update_product'),  # Update a product
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),  # Delete a product
    path('login/', TokenObtainPairView.as_view()),
    path('private/',views.private, name='private zone')
]
