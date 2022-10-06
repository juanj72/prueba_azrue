from .models import *
from django import forms

class formulario_persona(forms.ModelForm):
    class Meta():

     model=persona
     fields='__all__'
