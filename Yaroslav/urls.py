from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.ProductAPIView.as_view()),
    path('products/<int:pk>/', views.ProductAPIView.as_view()),
    path('basket/', views.BasketAPIView.as_view()),
    path('basket/<int:pk>/', views.BasketAPIView.as_view()),
]
