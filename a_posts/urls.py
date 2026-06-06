from django.urls import path
from .views import *

urlpatterns = [
    path('', post_page_view),
    path('<pk>/', post_page_view, name='post_page'),
    path('like/<pk>/', like_post, name='like_post'),
    path('bookmark/<pk>/', bookmark_post, name='bookmark_post'),
    path('comment/<uuid:pk>/', comment, name='comment'),
    path('comment/delete/<uuid:pk>/', comment_delete, name='comment_delete'),
    path('like_comment/<pk>/', like_comment, name='like_comment'),
    path('share_post/<pk>/', share_post, name='share_post'),
]
