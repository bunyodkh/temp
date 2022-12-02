from django.db.models.signals import post_save
from django.dispatch import receiver
from helpers.utils import path_and_rename

from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=path_and_rename('profiles/images'), blank=True, null=True)

    created = models.DateField()
    updated = models.DateField()


    class Meta:
        ordering = ['-created']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


    def __str__(self):
        return f'{self.user.username} Profile'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
