from PK2.models import File,Catalog
from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = File
        # Поля, которые мы сериализуем
        fields = ["id_file","name","size","extension","id_catalog"]
class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Catalog
        fields=["id_catalog","name"]