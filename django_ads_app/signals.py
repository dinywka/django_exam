from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User

@receiver(post_save, sender=UserProfile)
def create_user(sender, instance, created, **kwargs):
    if created:
        user = User(username=instance.user.username)
        user.set_unusable_password()
        user.save()
