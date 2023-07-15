from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find_words', views.find_words, name='find_words')
    # path('counter', views.counter, name='counter')
]