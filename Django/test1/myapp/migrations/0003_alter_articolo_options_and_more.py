# Generated by Django 4.2.6 on 2023-10-26 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_articolo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articolo',
            options={'verbose_name_plural': 'Articoli'},
        ),
        migrations.RenameField(
            model_name='articolo',
            old_name='data_creazopne',
            new_name='data_creazione',
        ),
    ]
