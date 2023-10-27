# Generated by Django 4.2.6 on 2023-10-27 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cognome', models.CharField(max_length=150)),
                ('lugo_nascita', models.CharField(max_length=150)),
                ('data_nascita', models.DateField()),
                ('data_inserimento', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Medici',
            },
        ),
    ]
