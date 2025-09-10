from django.urls import path
from .views import CareerPostListCreate, CareerPostDetail

urlpatterns = [
    # rota raiz: lista e cria
    path('', CareerPostListCreate.as_view(), name='posts-listcreate'),
    # rota com ID: detalhe, update, delete
    path('<int:pk>/', CareerPostDetail.as_view(), name='posts-detail'),
]
