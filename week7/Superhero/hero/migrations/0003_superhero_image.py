# Generated by Django 3.2.7 on 2021-09-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_superhero'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='image',
            field=models.CharField(default='image', max_length=200),
        ),
    ]
