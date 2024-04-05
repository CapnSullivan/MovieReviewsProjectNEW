from django.db import models


# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'основные новости'


    def __str__(self):
        return self.headline  # функция для определения названий статей в админке
