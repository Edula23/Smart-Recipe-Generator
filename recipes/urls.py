from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipesListView.as_view(), name="recipes-home"),
    path('about/', views.about, name="recipes-about"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
]