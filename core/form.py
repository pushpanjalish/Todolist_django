from dataclasses import fields
from pyexpat import model
from django import forms
from . models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model=ToDo
        fields='__all__'