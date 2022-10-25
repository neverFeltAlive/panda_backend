from django.db import models


class Application(models.Model):
    area_choices = {
        ('art', 'творческое'),
        ('sport', 'спортивное'),
        ('music', 'музыкальное')
    }
    age_choices = {
        ('small', 'младшая'),
        ('medium', 'средняя'),
        ('large', 'старшая'),
    }

    name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    phone_number = models.CharField(max_length=20, blank=False, verbose_name="Номер телефона")
    email = models.EmailField(max_length=50, blank=True, verbose_name="Электронная почта")
    group_age = models.CharField(max_length=15, blank=False, choices=age_choices, verbose_name="Возраст")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f'Заявка: {self.name} - {self.date}'


class Question(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    phone_number = models.CharField(max_length=20, blank=False, verbose_name="Номер телефона")
    email = models.EmailField(max_length=50, blank=True, verbose_name="Электронная почта")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f'Запись: {self.name} - {self.date}'


class Comment(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    comment = models.TextField(max_length=300, blank=False, verbose_name="Комментарий")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f'Комментарий: {self.name} - {self.date}'


class PhoneRequest(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    phone_number = models.CharField(max_length=20, blank=False, verbose_name="Номер телефона")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f'Заказ звонка: {self.name} - {self.date}'


class Picture(models.Model):
    image = models.FileField(upload_to="gallery/", null=True, verbose_name="Фотография")
    title = models.CharField(max_length=50, blank=True, default='', verbose_name="Название")
    text = models.TextField(max_length=300, blank=True, default='', verbose_name="Описание")

    def __str__(self):
        return self.title
