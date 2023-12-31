# Generated by Django 4.2.6 on 2023-11-18 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0005_alter_categorie_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indirizzo', models.CharField(max_length=250)),
                ('cap', models.CharField(max_length=20)),
                ('citta', models.CharField(max_length=100)),
                ('creato', models.DateTimeField(auto_now_add=True)),
                ('modificato', models.DateTimeField(auto_now=True)),
                ('pagato', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creato'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prezzo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantita', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ordini.order')),
                ('prodotto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.prodotti')),
            ],
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['-creato'], name='ordini_orde_creato_bc2554_idx'),
        ),
    ]
