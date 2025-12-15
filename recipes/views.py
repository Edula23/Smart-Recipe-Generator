from django.shortcuts import render, HttpResponse
recipes = [
    {
        'author': 'Eden',
        'title': 'Doro wet',
        'directions': 'combine all',
        'date_posted': 'May 19, 2021',
    },
    {
        'author': 'Naol',
        'title': 'Dinch wet',
        'directions': 'combine all',
        'date_posted': 'May 28, 2021',
    },
    {
        'author': 'Dawit',
        'title': 'Misr wet',
        'directions': 'combine all',
        'date_posted': 'May 09, 2021',
    }
]
# Create your views here.
def home(request):
    context = {
        'recipes': recipes,
        'title': 'Home',
    }
    return render(request, "recipes/home.html", context)
    # return HttpResponse("<h1>Welcome to my Recipes App </h1>")
def about(request):
    return render(request, "recipes/about.html", {'title': 'About'})
    # return HttpResponse("<h1>This is Recipes App to keep track of your recipes.</h1>")