from django.urls import path

from .views import *

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe_add'),
]

app_name = "recipes"
