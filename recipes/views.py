from django.shortcuts import render
from rest_framework import generics, response, status, permissions
from django.http import Http404
# Create your views here.
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
# creating a recipe

class RecipeCreate(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Recipe.objects.all()
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response({
                    "status": status.HTTP_200_OK,
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return response.Response({
                    "status": status.HTTP_400_bAD_REQUEST,
                    "data": serializer.errors,
                }
                )
class GetAllRecipes(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, *args, **kwargs):
        recipe = Recipe.objects.all()
        serializer = self.serializer_class(recipe, many=True)
        return response.Response({
            "status": status.HTTP_200_OK,
            "data": serializer.data
        }, status.HTTP_200_OK)
class GetSingleRecipe(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, *args, **kwargs):
        
        recipe_id = kwargs.get("id")
        recipe = Recipe.objects.filter(id = recipe_id)
        if recipe:
            serializer = self.serializer_class(recipe, many=True)
            return response.Response({
                "status": status.HTTP_200_OK,
                "data": serializer.data
            }, status.HTTP_200_OK)
        else:
            return response.Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Recipe with the above id doesn't exitst"
            }, status.HTTP_400_BAD_REQUEST)
class RecipeDelete(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    @staticmethod 
    def get_recipe_object(self, id, *args, **kwargs):
        try:
            return Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            raise Http404
    def delete(self, id, request, *args, **kwargs):
        recipe = self.get_recipe_object(id)
        recipe.delete(id)
        return response.Response({
            "status": status.HTTP_202_ACCEPTED,
            "message": "Recipe Deleted Successfully"
        }, status.HTTP_202_ACCEPTED)
        
class RecipeUpdate(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    @staticmethod 
    def get_recipe_object(id, *args, **kwargs):
        try:
            return Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            raise Http404
    def put(self, request, *args, **kwargs):  
        if request.method == "PUT":
            recipe_id = kwargs.get("id")
            recipe = self.get_recipe_object(recipe_id)
            serializer = self.serializer_class(recipe, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response({
                    "status": status.HTTP_202_ACCEPTED,
                    "message": "Recipe Updated "
                }, status.HTTP_202_ACCEPTED)
            else:
                return response.Response({
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Oops Something happended"                
                }, status.HTTP_400_BAD_REQUEST)
        