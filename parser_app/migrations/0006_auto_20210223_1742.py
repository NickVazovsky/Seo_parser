# Generated by Django 2.1.5 on 2021-02-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0005_auto_20210223_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='date_add',
            field=models.DateField(auto_now_add=True),
        ),
    ]
