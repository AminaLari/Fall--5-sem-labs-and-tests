from rest_framework import viewsets
from artist.serializers import ArtistsSerializer
from artist.models import Artists

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class =ArtistsSerializer # Сериализатор для модели

