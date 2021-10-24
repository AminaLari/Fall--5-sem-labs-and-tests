# используется для сортировки
from operator import itemgetter
class File:
    def __init__(self,id,name,size,extension,id_catalog):
        self.id=id
        self.name=name
        self.size=size
        self.extension=extension
        self.id_catalog=id_catalog
class Catalog:
    def __init__(self,id,name,):
        self.id=id
        self.name=name
class File_Catalog:
    def __init__(self,file_id,catalog_id):
        self.file_id=file_id
        self.catalog_id=catalog_id
files=[
    File(1,'Доклад по истории', 300,'.docx',3 ),
    File(2,'Фото с выпускного',63,'.png',1 ),
    File(3,'Summer song',46,'.mp3',2),
    File(4,'Учебник по литературе 10 класс',22450,'.pdf',3 ),
    File(5,'Фотография попугая',78,'.png',1),
    File(6,'Текст для презентации',458,'.docx',3),
    File(7,'Фильмы сборник',24780,'.mp4',4),
    File(8,'Фото3',57,'.png',5)
]
catalog=[
    Catalog(1,'Изображения'),
    Catalog(2,'Музыка'),
    Catalog(3,'Документы'),
    Catalog(4,'Видео'),
    Catalog(5,'Загрузки')
]
#Связи много-ко-многим
file_catalog=[
    File_Catalog(1,3),
    File_Catalog(1,5),
    File_Catalog(2,1),
    File_Catalog(2,3),
    File_Catalog(3,2),
    File_Catalog(4,3),
    File_Catalog(4,5),
    File_Catalog(5,1),
    File_Catalog(5,3),
    File_Catalog(6,3),
    File_Catalog(8,5),
    File_Catalog(8,1)
]
def main():
  # соединение данных один-ко-многим
  one_to_many=[
    (f.name,f.extension,c.name)
     for f in files
     for c in catalog
    if f.id_catalog==c.id
  ]
  # соединение данных много-ко-многим через промежуточную таблицу
  many_to_many_temp=[
      (c.name,c_f.file_id,c_f.catalog_id)
      for c in catalog
      for c_f in file_catalog
      if c.id == c_f.catalog_id
  ]
  many_to_many=[
      (f.name,f.extension,catalog_name)
      for catalog_name,file_id,catalog_id in many_to_many_temp
      for f in files if f.id==file_id
  ]
  print('Задание В1')
  b1=list(filter(lambda x:(str)(x[0]).startswith('Ф'),one_to_many))
  b1=[
      (el[0],el[2])
      for el in b1
  ]
  print(b1)
  print ('\nЗадание В2')
  res_unsorted=[]
  # перебираем все каталоги
  for c in catalog:
      #сравниваем id каталогов в файлах
      ct_files=list(filter(lambda i: i.id_catalog==c.id,files))
      #если каталог не пустой
      if len(ct_files)>0:
          min_size=min([f.size for f in ct_files])
          res_unsorted.append((c.name,min_size))
  # сортировка по минимальному размеру
  res_b2=sorted(res_unsorted,key=itemgetter(1),reverse=False)# сортировка размера по возрастанию
  print(res_b2)
  print('\nЗадание В3')
  b3=sorted(many_to_many,key=lambda y: y[0]) # сортировка по файлам
  print(b3)

if __name__ == '__main__':
  main()


