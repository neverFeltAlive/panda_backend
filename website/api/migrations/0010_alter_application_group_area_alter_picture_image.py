# Generated by Django 4.0.4 on 2022-07-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_application_group_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='group_area',
            field=models.CharField(choices=[('sport', 'спортивное'), ('art', 'творческое'), ('music', 'музыкальное')], max_length=15, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.FileField(null=True, upload_to='gallery/', verbose_name='Фотография'),
        ),
    ]