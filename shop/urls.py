from django.urls import path

from shop import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
]
