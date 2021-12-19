from rest_framework import viewsets
from PK2.serializers import FileSerializer,CatalogSerializer
from PK2.models import File,Catalog
from django.shortcuts import render

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

def GetFile(request):
    context={
        'data':File.objects.select_related('id_catalog') }
    return render (request,'datafromtables.html',context)

