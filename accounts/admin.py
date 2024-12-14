from django.contrib.auth.admin import UserAdmin as UserAdminDjango
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group as GroupDjango
from django.contrib.admin import site
from django.contrib import admin

from config import settings
from .models import User

site.site_title = settings.SITE_TITLE
site.site_header = settings.SITE_HEADER
site.index_title = settings.INDEX_TITLE
site.site_url = settings.SITE_URL

site.unregister(GroupDjango)


@admin.register(User)
class UserAdmin(UserAdminDjango):
    fieldsets = (
        (
            None,
            {"fields": (
                "username",
                "password",
            )}
        ),
        (
            _("Personal info"),
            {"fields": (
                "first_name",
                "last_name",
                "email",
                "phone",
            )}
        ),
        (
            _("Permissions"),
            {"fields": (
                "is_active",
                "role",
                "user_permissions",
            )},
        ),
        (
            _("Important dates"),
            {"fields": (
                "last_login",
                "date_joined",
            )}
        ),
    )
    list_display = (
        "username",
        "last_name",
        "first_name",
        "phone",
        "role",
        "is_active",
    )
    list_filter = (
        "role",
        "is_active",
    )
