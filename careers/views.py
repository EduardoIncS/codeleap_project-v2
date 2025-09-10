from rest_framework import generics, permissions
from .models import CareerPost, PostComment, PostLike
from .serializers import CareerPostSerializer, PostCommentSerializer, PostLikeSerializer

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

class PostLikeToggle(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs['pk']
        post = CareerPost.objects.get(pk=post_id)
        # Se já existir, remove; senão cria
        like, created = PostLike.objects.get_or_create(user=user, post=post)
        if not created:
            like.delete()

class PostCommentListCreate(generics.ListCreateAPIView):
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return PostComment.objects.filter(post_id=self.kwargs['pk']).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=self.kwargs['pk'])
