from django.urls import path

from . import views

app_name = 'sumtravel'

urlpatterns = [
    path("", views.index, name='index'),
    path('insert_restaurant/', views.insert_restaurant, name='insert_restaurant'),
    path('insert_restaurant/insert/', views.insert_restaurant_database, name='insert'),
    path("get_restaurants/", views.get_restaurant, name=''),
    path("get_restaurants/<int:restaurante_id>", views.restaurant, name=''),
    path("get_restaurants/filter/<int:restaurante_id>", views.restaurant_filter, name=''),

]
