from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'user_message', 'bot_response']
    search_fields = ['user_message', 'bot_response']
    list_filter = ['created_at']
