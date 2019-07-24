from django.contrib import admin
from django import forms
from .models import *

class data_mentor(forms.ModelForm):
    class Meta:
        model=Mentor
        fields=('nama','prof_pic','sebutan','pengalaman','quote',)

class data_mentee(forms.ModelForm):
    class Meta:
        model=Mentee
        fields=('nama','prof_pic','kesan')

class data_article(forms.ModelForm):
    class Meta:
        model=Article
        fields=('title','headline_pic','content')