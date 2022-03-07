from dataclasses import fields
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class Userform(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class Profileform(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    class Meta():
        model = Profile
        fields = ('portfolio_site', 'profile_pic')

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) != 0:
            raise forms.ValidationError('Bot presence recognized')