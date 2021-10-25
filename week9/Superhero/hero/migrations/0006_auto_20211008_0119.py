# Generated by Django 3.2.7 on 2021-10-08 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0005_auto_20211005_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='identity',
            field=models.CharField(default='--', max_length=200),
        ),
        migrations.AddField(
            model_name='hero',
            name='strength',
            field=models.CharField(default='--', max_length=500),
        ),
        migrations.AddField(
            model_name='hero',
            name='weakness',
            field=models.CharField(default='--', max_length=500),
        ),
        migrations.AlterField(
            model_name='hero',
            name='description',
            field=models.TextField(default='--'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.CharField(default='image', max_length=200),
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='identity',
            field=models.CharField(default='--', max_length=200),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='strength',
            field=models.CharField(default='--', max_length=500),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='weakness',
            field=models.CharField(default='--', max_length=500),
        ),
    ]
