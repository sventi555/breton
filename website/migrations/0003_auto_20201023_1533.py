# Generated by Django 3.1.2 on 2020-10-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201022_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='performance',
            name='resume',
            field=models.ImageField(upload_to=''),
        ),
    ]