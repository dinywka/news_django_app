from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import News, Category, Tags


# Create your views here.

"""

# 1. Сайт для подачи и просмотра новостей по категориям

User == django

Category == custom
(
id
name
)

Tag == custom (ключевое слово)
(
id
name
)

News == custom
(
id
title
category -- OneToMany
tags -- ManyToMany
)

"""



def home(request):
    return render(request, "home.html")


def add_news_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        tags_ids = request.POST.getlist('tags[]')

        category = Category.objects.get(id=category_id)
        news = News(title=title, category=category)
        news.save()

        for tag_id in tags_ids:
            tag = Tags.objects.get(id=tag_id)
            news.tags.add(tag)

        request.session['title'] = title
        request.session['tags'] = tags_ids
        request.session['category'] = category_id

        return redirect('all_news')

    categories = Category.objects.all()
    tags = Tags.objects.all()
    context = {
        'categories': categories,
        'tags': tags
    }
    return render(request, 'news_form.html', context)

def all_news(request):
    all_news = News.objects.all()


    context = {
        'news': all_news
    }
    return render(request, 'all_news.html', context)

