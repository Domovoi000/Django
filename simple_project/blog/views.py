from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.


def home(request):
    posts = Article.objects.order_by('-created_at')

    return render(request, 'blog/home.html', {'posts': posts})


def test(request):
    return HttpResponse('<h1>Test</h1>')