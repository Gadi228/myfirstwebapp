from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('<slug:slug>', views.PostListView.as_view(), name='post_list'),
    path('recipe', views.Recipe, name='recipe'),
]
