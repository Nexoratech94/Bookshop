# Generated by Django 5.0.4 on 2024-04-23 07:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0004_book_condition'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('delivery_charge', models.DecimalField(decimal_places=2, default=100.0, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='Eshop.CartItem', to='Eshop.book'),
        ),
    ]
