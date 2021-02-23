# Generated by Django 2.1.5 on 2021-02-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0004_auto_20210223_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='base_url',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='broken_link',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='description',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='description_unique',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='facebook',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='google',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='h1',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='h2',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='instagram',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='keywords',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='title',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='title_unique',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='url',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='vk',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='results',
            name='yandex',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
    ]