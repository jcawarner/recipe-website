from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<str:food>', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('recipe/', views.recipe, name='recipe'),
    path('search/', views.search, name='search'),
    path('random/', views.random, name='random'),
    path('random-recipe/', views.random_recipe, name='random_recipe'),
    path('menu/', views.menu, name='menu'),
    path('meats/<int:id>', views.meats, name='meats')

]