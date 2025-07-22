from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from accounts.forms import AppUserCreationForm

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(DefaultUserAdmin):
    list_display = ("email", "is_staff", "is_active")
    add_form = AppUserCreationForm
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    # 🔒 Secure role management
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if not request.user.is_superuser:
            form.base_fields['groups'].disabled = True
            form.base_fields['user_permissions'].disabled = True

        return form

    def has_module_permission(self, request):
        # Optional: completely hide the Users section for staff
        if not request.user.is_superuser:
            return False
        return super().has_module_permission(request)