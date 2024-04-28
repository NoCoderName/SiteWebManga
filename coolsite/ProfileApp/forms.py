from django import forms

from django.contrib.auth import get_user_model


# Поменять название
class ProfileForm(forms.ModelForm):
    delete = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = get_user_model()
        fields = ('delete',)
        
