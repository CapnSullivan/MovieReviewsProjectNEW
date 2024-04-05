from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/static/')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'КИНОФИЛЬМЫ'
        verbose_name_plural = 'кино'

    def __str__(self):
        return self.title  # функция для определения названий кино в админке


class Review(models.Model):
        # содержит текст обзора
    text = models.CharField(max_length=100)
        # содержит время добавления орбзора и обновления
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

        # ForeignKey - отношение один ко многим (Пользователь - множество обзоров)
    user = \
        models.ForeignKey(User, on_delete=models.CASCADE)
    movie = \
        models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text
