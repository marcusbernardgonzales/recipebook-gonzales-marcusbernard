from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'ledger/recipe_list.html', ctx)
    
def recipe_detail(request, pk):
    ctx = { 'recipe': Recipe.objects.get(id=pk) }
    return render(request, 'ledger/recipe.html', ctx)
