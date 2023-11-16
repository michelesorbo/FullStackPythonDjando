# Generated by Django 4.2.6 on 2023-11-16 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_userprofile_cap_userprofile_citta_userprofile_comune_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cf',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Inserisci un Codice Fiscale valido', regex='^[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}$')], verbose_name='Codice Fiscale'),
        ),
    ]
