from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'ledger/recipe_list.html', ctx)


@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'ledger/recipe.html', {
        "recipe": recipe,
    })


class RecipeCreateView(LoginRequredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_add.html'
