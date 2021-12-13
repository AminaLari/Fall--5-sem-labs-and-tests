from artist.models import Artists
from rest_framework import serializers

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Artists
        fields=['id','name','country','arts','is_impressionism']
