# Generated by Django 3.2.15 on 2022-09-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veganapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organ',
            name='name',
            field=models.CharField(choices=[('Eye', 'Eye'), ('Hair', 'Hair'), ('Brain', 'brain'), ('Lungs', 'lungs'), ('Heart', 'heart'), ('Muscles', 'Muscles'), ('Bones', 'Bones'), ('Skin', 'Skin'), ('Bowels', 'Bowels')], max_length=50, unique=True),
        ),
    ]
