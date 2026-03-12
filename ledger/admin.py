from django.contrib import admin
from .models import Recipe, RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeImageInline, ]


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

admin.site.register(Recipe, RecipeAdmin)


