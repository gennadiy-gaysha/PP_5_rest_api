from django.db import models
from django.contrib.auth.models import User
from paintings.models import Painting

class Observation(models.Model):
    """
    Observation model, related to 'owner' and 'painting'.
    'owner' is a User instance and 'painting' is a Painting instance.
    'unique_together' makes sure a user can't observe the same painting twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE,
                                 related_name='observations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
        unique_together = [['owner', 'painting']]

    def __str__(self):
        return f"{self.owner} {self.painting}"