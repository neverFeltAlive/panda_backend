# Generated by Django 4.0.4 on 2022-07-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_pictures_alter_application_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='group_age',
            field=models.CharField(choices=[('large', 'старшая'), ('medium', 'средняя'), ('small', 'младшая')], max_length=15, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.FileField(null=True, upload_to='gallery/', verbose_name='Фотография'),
        ),
    ]
