from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "recipes/home.html")
    # return HttpResponse("<h1>Welcome to my Recipes App </h1>")
def about(request):
    return render(request, "recipes/about.html")
    # return HttpResponse("<h1>This is Recipes App to keep track of your recipes.</h1>")