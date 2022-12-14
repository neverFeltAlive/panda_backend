# Generated by Django 4.0.4 on 2022-10-25 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_application_group_area_remove_comment_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='group_age',
            field=models.CharField(choices=[('small', 'младшая'), ('medium', 'средняя'), ('large', 'старшая')], max_length=15, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=300, verbose_name='Комментарий'),
        ),
    ]
