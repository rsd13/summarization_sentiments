from django.urls import path

from . import views

app_name = 'sumtravel'

urlpatterns = [
    path("", views.index, name='index'),
    path('find_restaurant', views.get_restaurant, name='get_restaurant',),
    path('find_restaurant/insert/', views.insert_restaurant, name='insert'),

]
