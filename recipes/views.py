from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
        'title': 'Home',
    }
    return render(request, "recipes/home.html", context)
    # return HttpResponse("<h1>Welcome to my Recipes App </h1>")
class RecipesListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
class RecipeDetailView(DetailView):
    model = models.Recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
def about(request):
    return render(request, "recipes/about.html", {'title': 'About'})
    # return HttpResponse("<h1>This is Recipes App to keep track of your recipes.</h1>")