from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'username', 'email', 'first_name', 'last_name', 'bio', 'role')
    list_editable = ('role',)
    search_fields = ('username', 'email',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
