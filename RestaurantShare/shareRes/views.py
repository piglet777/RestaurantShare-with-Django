from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'index.html', content)

def restaurantDetail(request):
    # return HttpResponse("restaurantDetail")
    return render(request, 'restaurantDetail.html')

def restaurantCreate(request):
    # return HttpResponse("restaurantCreate")
    return render(request, 'restaurantCreate.html')

def categoryCreate(request):
    # return HttpResponse("categoryCreate")
    return render(request, 'categoryCreate.html')

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
