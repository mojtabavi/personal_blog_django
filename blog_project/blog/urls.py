from django.urls import path
from .views import detail, category, author,ArticleList

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('p<int:page>', ArticleList.as_view(), name="home"),
    path('article/<slug:slug>', detail, name="detail"),
    path('category/<slug:slug>', category, name="category"),
    path('category/<slug:slug>/p<int:page>', category, name="category"),
    path('auth/<slug:username>', author, name="author"),
    path('auth/<slug:username>/p<int:page>', author, name="author"),

]