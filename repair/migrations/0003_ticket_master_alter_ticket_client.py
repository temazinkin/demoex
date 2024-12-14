# Generated by Django 5.1.4 on 2024-12-14 09:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_ticket'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_tickets', to=settings.AUTH_USER_MODEL, verbose_name='мастер'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_tickets', to=settings.AUTH_USER_MODEL, verbose_name='клиент'),
        ),
    ]