from django import forms
from .models import ChatMessage

class ChatForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['user_message']
        widgets = {
            'user_message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your message...',
                'rows': 1
            })
        }
