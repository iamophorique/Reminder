from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'remind_at', 'is_sent', 'created_at')
    list_filter = ('is_sent', 'remind_at')
    search_fields = ('message', 'user__username')
    ordering = ('remind_at',)
