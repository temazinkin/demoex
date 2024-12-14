# Generated by Django 5.1.4 on 2024-12-14 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_ticket_master_alter_ticket_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='client',
            field=models.ForeignKey(limit_choices_to={'role': 'client'}, on_delete=django.db.models.deletion.CASCADE, related_name='my_tickets', to=settings.AUTH_USER_MODEL, verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='master',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'master'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_tickets', to=settings.AUTH_USER_MODEL, verbose_name='мастер'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата и время')),
                ('text', models.CharField(max_length=255, verbose_name='текст')),
                ('minutes', models.PositiveIntegerField(default=10, verbose_name='затрачено времени')),
                ('money', models.PositiveIntegerField(default=500, verbose_name='затрачено рублей')),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair.ticket', verbose_name='заявка')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ['-created'],
            },
        ),
    ]
