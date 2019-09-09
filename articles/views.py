from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {'article': article}
    return render(request, 'articles/index.html', context)

def create(request):
    return render(request, 'articles/create.html')

def read(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()
    return redirect(f'/articles/{article.pk}/detail')

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article' : article}
    return render(request, 'articles/update.html', context)

def read_update(request, article_pk):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article.objects.get(pk=article_pk)
    article.title = title
    article.content = content
    article.save()
    return redirect(f'/articles/{article.pk}/detail')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect(f'/articles/')
