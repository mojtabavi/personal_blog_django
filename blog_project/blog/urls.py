from django.urls import path
from .views import home, detail, category, author

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('p<int:page>', home, name="home"),
    path('article/<slug:slug>', detail, name="detail"),
    path('category/<slug:slug>', category, name="category"),
    path('category/<slug:slug>/p<int:page>', category, name="category"),
    path('auth/<slug:username>', author, name="author"),
    path('auth/<slug:username>/p<int:page>', author, name="author"),

]