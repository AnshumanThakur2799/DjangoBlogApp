from django.urls import path
from .views import ListView,CreatePostView, PostRetrieveUpdateDeleteView, PostComment,EditComment

urlpatterns = [
    path('posts/', ListView.as_view(), name='post-list'),
    path('posts/create/', CreatePostView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', PostComment.as_view(), name='post-comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', EditComment.as_view(), name='edit-comment'),
]
