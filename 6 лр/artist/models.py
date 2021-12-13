from django.db import models

class Artists(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя художника")
    country=models.CharField(max_length=40, verbose_name="Страна")
    arts=models.CharField(max_length=100, verbose_name="Известные работы")
    is_impressionism = models.BooleanField(verbose_name="Художник работал в жанре импрессионизм?")

