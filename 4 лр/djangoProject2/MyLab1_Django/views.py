from django.shortcuts import render

def GetArtists(request):
    return render(request, 'master.html', {'data':{'artists':
    [
        {'title': 'Анри Матисс', 'id':1},
        {'title': 'Клод Моне','id':2},
        {'title': 'Эдгар Дега','id':3},
    ]
    }})

def GetArtist(request,id):
    return render(request,'detail.html',{'data':{
        'id':id,
        'arts':[
           {'name':'"Красные рыбы"','style':'Экспрессионизм','materials':'Холст,масло','year':'1912 г.','id':1},
           {'name':'"Белые кувшинки"','style':'Импрессионизм', 'materials': 'Холст,масло', 'year': '1899 г.','id':2},
           {'name':'"Голубые танцовщицы"','style':'Импрессионизм', 'materials': 'Бумага,пастель', 'year':'Около 1898 г.','id':3},
        ]
    }})
