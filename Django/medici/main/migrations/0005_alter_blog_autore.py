# Generated by Django 4.2.6 on 2023-11-06 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_blog_autore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='autore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]