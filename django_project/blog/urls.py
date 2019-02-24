from django.urls import path, include, re_path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    MyFormView,
    CommentDeleteView,
    PostAllListView

)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('all', PostAllListView.as_view(), name='blog-home-all'),
    path('promotions/', include('promotion.urls')),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', MyFormView.as_view(), name='my_form_view_url'),
    path('post/new/<int:promotion_id>/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/<int:promotion_id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/join/<int:pk>/', views.joinsplit, name='join-split'),
    path('post/quit/<int:pk>/', views.quitsplit, name='quit-split'),
    path('about/', views.about, name='blog-about'),
]
