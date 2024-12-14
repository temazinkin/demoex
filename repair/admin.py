from django.contrib import admin

from accounts.models import Role
from .models import Appliance, Ticket, Comment


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = False
    extra = 1
    readonly_fields = (
        'author',
    )
    fields = (
        'author',
        'text',
        'minutes',
        'money',
    )

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = (
        "__str__",
        "client",
        "client__phone",
        "master",
    )

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Comment):
                if not instance.author:
                    instance.author = request.user
            instance.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.role == Role.CLIENT:
            queryset = queryset.filter(client=request.user)
        return queryset

    def has_change_permission(self, request, obj=None):
        if request.user.role == Role.CLIENT:
            if obj and obj.master:
                return False
        return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.role == Role.CLIENT:
            return (
                "master",
                "client",
            )
        return []

    def get_list_filter(self, request):
        if request.user.role == Role.CLIENT:
            return []
        return (
            "master",
            "appliance",
        )
