from django.urls import path

from app import views

urlpatterns = [
    path("", views.home),
    path('add-news/', views.add_news_view, name='add_news'),
    path('all_news/', views.all_news, name='all_news')
]
