import django_filters
from .models import Profile
from django import forms


class MistriFilter(django_filters.FilterSet):
    
    class Meta:
        model=Profile
        fields={'address','skill'}
 