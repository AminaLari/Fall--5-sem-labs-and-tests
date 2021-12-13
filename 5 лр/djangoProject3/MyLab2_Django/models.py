from django.db import models

# Create your models here.
class Artists(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'artists'

class Art(models.Model):
    name=models.CharField(max_length=60)
    materials=models.CharField(max_length=50)
    artistid=models.ForeignKey('Artists',models.DO_NOTHING,db_column='artistid',blank=True,null=True)
    class Meta:
        managed=False
        db_table='art'
# Create your models here.
