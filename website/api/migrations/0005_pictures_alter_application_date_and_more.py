# Generated by Django 4.0.4 on 2022-07-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_application_remove_question_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='../../frontend/public/images/gallery', verbose_name='Фотография')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(default='', max_length=300, verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='application',
            name='group_age',
            field=models.CharField(choices=[('large', 'старшая'), ('small', 'младшая'), ('medium', 'средняя')], max_length=15, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='application',
            name='group_area',
            field=models.CharField(choices=[('art', 'творческое'), ('music', 'музыкальное'), ('sport', 'спортивное')], max_length=15, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=300, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='phonerequest',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='phonerequest',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='phonerequest',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='question',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(default='', max_length=300, verbose_name='Вопрос'),
        ),
    ]