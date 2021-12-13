from MyLab2_Django.models import Artists
from MyLab2_Django.models import Art
from django.shortcuts import render
from datetime import date

def Artistslist(request):
    return render(request, 'artists.html', {'data' : {
        'current_date': date.today(),
        'artists': Artists.objects.all() #запрос
    }})

def GetArtist(request, id):
    ar=Artists.objects.get(id=id)
    context={
        'id':ar.id,
        'name':ar.name,
        'country':ar.country,
    }
    return render(request,'artist.html',context)

def GetArt(request,id):
    ar=Art.objects.get(id=id)
    context={
        'id':ar.id,
        'name':ar.name,
        'materials':ar.materials,
    }
    return render(request, 'art.html',context)



