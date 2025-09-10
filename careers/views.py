from rest_framework import generics
from .models import CareerPost
from .serializers import CareerPostSerializer

class CareerPostListCreate(generics.ListCreateAPIView):
    """
    • GET  /careers/    → lista todos os posts (imagem 2)
    • POST /careers/    → criar novo post (imagem 2)
    """
    queryset         = CareerPost.objects.all().order_by('-created_datetime')
    serializer_class = CareerPostSerializer

class CareerPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    • GET    /careers/<id>/    → detalhar um post (imagem 2)
    • PATCH  /careers/<id>/    → atualiza title e/ou content (imagem 3)
    • PUT    /careers/<id>/    → substitui todos os campos editáveis
    • DELETE /careers/<id>/    → deleta o post (imagem 3)
    """
    queryset         = CareerPost.objects.all()
    serializer_class = CareerPostSerializer
