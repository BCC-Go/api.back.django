from django.contrib import admin
from .models import User

@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    search_field = ('name', 'consumption')
    list_display = [
        'id',
        'login_id',
        'name',
        'rank_id',
        'phone',
        'consumption',
        'type',
    ]
    list_display_links = ['id', 'name']
    ordering = ['id']
