from django_filters import rest_framework as df_filters
from .models import Painting

class PaintingFilter(df_filters.FilterSet):
    class Meta:
        model = Painting
        fields = ['theme', 'technique', 'availability']