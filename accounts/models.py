from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class Role(models.TextChoices):
    CLIENT = 'client', 'Клиент'
    MASTER = 'master', 'Мастер'
    OPERATOR = 'operator', 'Оператор'


class User(AbstractUser):
    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    phone = models.CharField(
        "телефон",
        max_length=20,
        blank=True,
    )
    role = models.CharField(
        'роль',
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
