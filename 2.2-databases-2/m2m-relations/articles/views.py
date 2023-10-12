from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    # ordering = '-published_at'
    articles = Article.objects.all()
    context['articles'] = articles
    return render(request, template, context)
