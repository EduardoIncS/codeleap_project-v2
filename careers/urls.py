from django.urls import path
from .views import CareerPostListCreate, CareerPostDetail, PostCommentListCreate, PostLikeToggle

urlpatterns = [
    path('', CareerPostListCreate.as_view(), name='posts-listcreate'),
    path('<int:pk>/', CareerPostDetail.as_view(), name='posts-detail'),
    path('<int:pk>/like/', PostLikeToggle.as_view(), name='posts-like'),
    path('<int:pk>/comments/', PostCommentListCreate.as_view(), name='posts-comments'),
]
