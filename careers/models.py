from django.db import models
from django.conf import settings

class CareerPost(models.Model):
    username         = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title            = models.CharField(max_length=200)
    content          = models.TextField()

    def __str__(self):
        return f"{self.username} — {self.title}"

class PostLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(CareerPost, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(CareerPost, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class PostAttachment(models.Model):
    post = models.ForeignKey(CareerPost, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
