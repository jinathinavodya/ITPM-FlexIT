from django.forms import ModelForm
from .models import *
from dataclasses import fields

from django.forms import ModelForm
from django import forms

class vacancyform(ModelForm):
        class Meta:
            model = vacancy
            fields = '__all__'

class CvDetailsForm(ModelForm):
    class Meta:
        model = Cvdetails
        fields = '__all__'
    