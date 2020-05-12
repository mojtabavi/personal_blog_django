from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article

# Create your views here.

#first page of site
def home(request):

    articles = Article.objects.filter(status="p").order_by('-publish')
    context = {
        "articles" : articles
            
    }
    return render(request, 'blog/home.html',context)


def detail(request, slug):
     
    context = {
        "article" : Article.objects.get(slug=slug)
        
            
    }
    return render(request, 'blog/detail.html',context)