from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))


class Profile(models.Model):
    """
    Represents a user profile linked to the User model in a one-to-one
    relationship. It includes personal details about the user such as name,
    bio, home country, gender, birthdate, and a profile image. It automatically
    handles the creation and updates of timestamps when a profile is created or
    modified.

    Meta:
        ordering: Profiles are ordered by their creation time in descending
        order.

    Methods:
        __str__: Returns a string representation of the profile, which is
        "<username>'s profile".
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    home_country = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='../default_profile_h0pgqr')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

    @property
    def email(self):
        """Method acts as a bridge to access the email field from the User
        model, ensuring that we always get the current email of the user
        associated with a profile. Not strictly necessary for the purpose of
        this project, since we have the email field in ProfileSerializer.
        """
        return self.owner.email


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a Profile instance automatically whenever a
    User instance is created.
    """
    if created:
        Profile.objects.create(owner=instance)
