from django.urls import path
from .views import HomeView, PostListView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pages/', PostListView.as_view(), name='post_list'),
    path('pages/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
