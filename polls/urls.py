# polls/urls.py
from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Question

app_name = 'polls'

urlpatterns = [
    path(
        '', 
        ListView.as_view(model=Question, template_name='polls/index.html'), 
        name='index'
    ),
    path(
        '<int:pk>/', 
        DetailView.as_view(model=Question, template_name='polls/detail.html'), 
        name='detail'
    ),
    path(
        '<int:pk>/results/', 
        DetailView.as_view(model=Question, template_name='polls/results.html'), 
        name='results'
    )
]

