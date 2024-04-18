from django.db import models
from django.contrib.auth.models import User

TECHNIQUE_CHOICES = (
    ('Oil Paint', 'Oil Paint'), ('Acrylic Paint', 'Acrylic Paint'),
    ('Watercolor', 'Watercolor'), ('Gouache', 'Gouache'),
    ('Pastel', 'Pastel'), ('Charcoal', 'Charcoal'), ('Graphite', 'Graphite'),
    ('Ink', 'Ink'), ('Mixed Media', 'Mixed Media'),)

THEME_CHOICES = (
    ('Portrait', 'Portrait'), ('Still Life', 'Still Life'),
    ('Landscape', 'Landscape'), ('Seascape', 'Seascape'),
    ('Abstract', 'Abstract'), ('Figurative', 'Figurative'), ('Genre', 'Genre'),
    ('Animal', 'Animal'), )


class Painting(models.Model):
    """
    Represents a painting created by a user. This model includes details about
    the painting such as title, creation year, technique, theme, dimensions,
    price, and an image of the painting.

    Meta:
        ordering: Orders paintings by the creation time in descending order.

    Methods:
        __str__: Returns a string representation of the painting, including its
        ID and title.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    creation_year = models.PositiveIntegerField(blank=True)
    technique = models.CharField(max_length=25, choices=TECHNIQUE_CHOICES)
    theme = models.CharField(max_length=25, choices=THEME_CHOICES)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='images/', default='../default_painting_czwroy', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
