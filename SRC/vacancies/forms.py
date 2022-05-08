from django.forms import ModelForm
from .models import  vacancy
from dataclasses import fields

from django import forms

class vacancyform(ModelForm):
        class Meta:
            model = vacancy
            fields = '__all__'
    