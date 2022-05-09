from email import message
import imp
from unicodedata import category
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages

def index(request):
    return render(request,"base/layout.html")
# Create your views here.

class CategoryView(View):
    def get(self,request):
        categories = Category.objects.all()
        context = {
            'categories':categories
        }
        return render(request,"category/index.html",context)
    
    def post(self,request):
        category_name = request.POST['category_name']
        category = Category(category_name=category_name)
        category.save()
        messages.info(request,"successfully create new category")

        return redirect("category")
    

def delete_category(request,id):
    category = Category.objects.filter(id=id).first()
    if category:
        category.delete()
        messages.info(request,"successfully delete category")
    return redirect("category")



def update_category(request,id):
    category = Category.objects.filter(id=id).first()
    if request.method == 'POST':
        category.category_name = request.POST['category_name']
        category.save()
        messages.info(request,"successfully update the category")
        return redirect("category")
        

    context = {
        'category':category
    }
    return render(request,"category/update.html",context)