# Generated by Django 4.2.6 on 2023-11-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_pazienti_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='medici',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
