from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sum/', views.sum),
    path('difference/', views.difference),
    path('multiply/', views.multiply),
    path('divide/', views.divide),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
