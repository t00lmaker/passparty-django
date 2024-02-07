from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Client, Preferences


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'username', 'role', 'client', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    search_fields = ('email', 'username', 'client__name')
    list_filter = ('client__name','role', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('client', 'role')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'client', 'role'),
        }),
    )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'phone', 'email', 'created_at', 'updated_at')
    fields = ('name', 'phone', 'email')
    search_fields = ('name',)

@admin.register(Preferences)
class PreferencesAdmin(admin.ModelAdmin):
    ordering = ('client','key')
    fields = ('client','key','value',)
    list_display = ('client', 'key', 'value', 'created_at', 'updated_at')
    list_filter = ('client__name',)
    search_fields = ('client__name',)