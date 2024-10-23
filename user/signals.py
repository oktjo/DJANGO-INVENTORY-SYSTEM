#use to automatically create profiles without repeating
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver #used to decorate like permit post save

@receiver(post_save, sender=User)
def create_profile(sender, instance,created, **kwargs):
	if created:
		Profile.objects.create(staff=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
	#go to app,py and register

