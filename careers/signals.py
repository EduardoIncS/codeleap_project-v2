import re
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CareerPost

def notify_mentions(instance):
    users = set(re.findall(r'@(\w+)', instance.content))
    User = get_user_model()
    for uname in users:
        try:
            user = User.objects.get(username=uname)
        except User.DoesNotExist:
            pass

@receiver(post_save, sender=CareerPost)
def career_post_mentions_handler(sender, instance, created, **kwargs):
    notify_mentions(instance)
