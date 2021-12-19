from django.db import models

class File(models.Model):
    id_file = models.AutoField('id_file', primary_key=True)
    name = models.CharField(max_length=40, verbose_name="Название")
    size = models.IntegerField(verbose_name="Размер")
    extension = models.CharField(max_length=20, verbose_name="Расширение")
    id_catalog = models.ForeignKey('Catalog',models.DO_NOTHING, db_column='id_catalog')

    class Meta:
        managed=False
        db_table='PK2_file'

class Catalog(models.Model):
    id_catalog=models.AutoField('id_catalog',primary_key=True)
    name=models.CharField(max_length=20,verbose_name="Каталог")
    class Meta:
        managed=False
        db_table='PK2_catalog'


