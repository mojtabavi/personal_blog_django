from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Article, Category

# Create your views here.

#first page of site
def home(request):

    articles = Article.objects.published().order_by('-publish')
    
    context = {
        "articles" : articles,
        
            
    }
    return render(request, 'blog/home.html',context)


def detail(request, slug):
    context = {
        "article" : get_object_or_404(Article.objects.published(), slug=slug)            
    }
    return render(request, 'blog/detail.html',context)


def category(request, slug):
    context = {
        "category" : get_object_or_404(Category, slug=slug, status=True)            
    }
    return render(request, 'blog/category.html',context)