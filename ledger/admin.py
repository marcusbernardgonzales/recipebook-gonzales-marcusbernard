from django.contrib import admin
from .models import Recipe, RecipeImage


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeImageInline, ]


admin.site.register(Recipe, RecipeAdmin)
