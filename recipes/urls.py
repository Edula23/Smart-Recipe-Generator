from django.urls import path
from recipes.views import RecipeCreate, GetAllRecipes, RecipeDelete, GetSingleRecipe, RecipeUpdate

urlpatterns = [
    path('create/', RecipeCreate.as_view(), name="create-recipe"),
    path('get-all-recipes/', GetAllRecipes.as_view(), name="get-all-recipes"),
    path('get/<int:id>/', GetSingleRecipe.as_view(), name="get-single-recipe"),
    path('update/<int:id>/', RecipeUpdate.as_view(), name="recipe-update"),
    path('delete/<int:id>/', RecipeDelete.as_view(), name="recipe-delete"),
]