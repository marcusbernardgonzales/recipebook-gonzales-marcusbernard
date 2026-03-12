from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView

from .models import Recipe
from .forms import RecipeForm, RecipeImageForm


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


@login_required
def add_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeImageForm()

    return render(request, 'ledger/recipeimage_add.html', {
        "form": form,
        "recipe": recipe,
    })


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_add.html'
