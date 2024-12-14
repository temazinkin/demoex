from django.db import models

from accounts.models import Role


class Appliance(models.Model):
    name = models.CharField(
        'название',
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'вид'
        verbose_name_plural = 'бытовая техника'


class Ticket(models.Model):
    created = models.DateTimeField(
        'дата добавления',
        auto_now_add=True,
    )
    appliance = models.ForeignKey(
        'Appliance',
        verbose_name='вид техники',
        on_delete=models.CASCADE,
    )
    model = models.CharField(
        'модель техники',
        max_length=100,
        blank=True,
    )
    client = models.ForeignKey(
        'accounts.User',
        related_name='my_tickets',
        verbose_name='клиент',
        on_delete=models.CASCADE,
        limit_choices_to={'role': Role.CLIENT},
    )
    master = models.ForeignKey(
        'accounts.User',
        related_name='client_tickets',
        verbose_name='мастер',
        on_delete=models.CASCADE,
        limit_choices_to={'role': Role.MASTER},
        blank=True,
        null=True,
    )
    description = models.TextField(
        'описание проблемы',
        blank=True,
    )

    def __str__(self):
        return f'Заявка № {self.pk}'

    class Meta:
        verbose_name = 'тикет'
        verbose_name_plural = 'заявки на ремонт'


class Comment(models.Model):
    created = models.DateTimeField(
        'дата и время',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        'accounts.User',
        verbose_name='автор',
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
    )
    ticket = models.ForeignKey(
        'Ticket',
        verbose_name='заявка',
        on_delete=models.CASCADE,
    )
    text = models.CharField(
        'текст',
        max_length=255,
    )
    minutes = models.PositiveIntegerField(
        'затрачено времени',
        default=10,
    )
    money = models.PositiveIntegerField(
        'затрачено рублей',
        default=500,
    )

    def __str__(self):
        return f'{self.created:%H:%M %d.%m.%Y}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['-created']
