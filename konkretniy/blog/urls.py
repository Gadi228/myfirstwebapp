from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_detail'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('recipe', views.recipe, name='recipe'),
]
