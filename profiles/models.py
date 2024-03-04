from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'))

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    home_country = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    # The upload_to='images/' argument specifies that uploaded images for this
    # field should be stored in the images/ directory in Cloudinary. This path
    # is appended to the base Cloudinary storage location.
    image = models.ImageField(upload_to='images/', default='../default_profile_h0pgqr')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

    @property
    def email(self):
        """Method acts as a bridge to access the email field from the User model,
        ensuring that we always get the current email of the user associated with
        a profile.
        """
        return  self.owner.email

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

