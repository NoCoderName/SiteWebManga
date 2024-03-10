from django import forms

from .models import *


class CommentForm(forms.ModelForm):
    message = forms.CharField(label='Оставить коментарий', widget=forms.TextInput(attrs={'class': 'message-input'}))
    
    class Meta: 
        model = Comment
        fields = ('message',)