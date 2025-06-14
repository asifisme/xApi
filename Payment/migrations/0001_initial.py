# Generated by Django 5.2.1 on 2025-06-01 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xApiCart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name_of_payer', models.CharField(blank=True, max_length=255, null=True)),
                ('email_of_payer', models.EmailField(blank=True, max_length=254, null=True)),
                ('amount_paid', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('stripe_checkout_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('stripe_payment_intent', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('stripe_payment_status', models.CharField(blank=True, max_length=50, null=True)),
                ('stripe_payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('receipt_url', models.URLField(blank=True, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='xApiCart.ordermodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
