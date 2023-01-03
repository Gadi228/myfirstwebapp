from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('recipe', views.recipe, name='recipe'),
]
