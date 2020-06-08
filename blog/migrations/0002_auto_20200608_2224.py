# Generated by Django 3.0.7 on 2020-06-08 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-modify_date',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='', verbose_name='CONTENT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Create Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='설명글', max_length=100, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modify Date'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', help_text='One word for title alias.', unique=True, verbose_name='SLUG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='TITLE'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='post',
            table='my_post',
        ),
    ]
