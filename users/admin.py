from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined')

admin.site.register(User, UserAdmin)
