# Generated by Django 2.1.5 on 2021-02-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0002_auto_20210223_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteWhileSaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keyrwords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
