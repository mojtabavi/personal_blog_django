from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Article, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

#first page of site
def home(request, page=1):

    article_list = Article.objects.published().order_by('-publish')
    paginator = Paginator(article_list, 3)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    context = {
        "articles" : articles,
        
            
    }
    return render(request, 'blog/home.html',context)


def detail(request, slug):
    context = {
        "article" : get_object_or_404(Article.objects.published(), slug=slug)            
    }
    return render(request, 'blog/detail.html',context)


def category(request, slug, page=1):
    category_obj = get_object_or_404(Category, slug=slug, status=True)
    category_list = category_obj.articles.published()
    paginator = Paginator(category_list, 3)

    try:
        articles_cg = paginator.page(page)
    except PageNotAnInteger:
        articles_cg = paginator.page(1)
    except EmptyPage:
        articles_cg = paginator.page(paginator.num_pages)
    
    context = {
        "category" : category_obj,
        "articles" : articles_cg,            
    }
    return render(request, 'blog/category.html',context)