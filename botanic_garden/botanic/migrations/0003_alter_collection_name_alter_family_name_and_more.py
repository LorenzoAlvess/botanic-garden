# Generated by Django 5.0.7 on 2024-07-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botanic', '0002_family_description_genus_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(help_text='Name of the collection.', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(help_text='Name of the family.', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='genus',
            name='name',
            field=models.CharField(help_text='Name of the genus.', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(help_text='Name of the species.', max_length=255, unique=True),
        ),
    ]