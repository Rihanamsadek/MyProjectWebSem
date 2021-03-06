from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from Recipes.models import Recette


def home(request):
    latest_recipe_list = Recette.objects.order_by('-pub_date')[:5]
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')


def detail(request, recipe_id):
    recipe = get_object_or_404(Recette, pk=recipe_id)
    return render(request, 'Recipes/detail.html', {'recipe': recipe})


def myrecipe(request):
    return render(request, 'Recipes/myRecipe.html')


def cookbook(request):
    latest_recipe_list = Recette.objects.order_by('-pub_date')
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'Recipes/cookbook.html', context)
