from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDeleteView, LikeListCreateView, LikeRetrieveUpdateDeleteView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeRetrieveUpdateDeleteView.as_view(), name='like-retrieve-update-delete'),
]