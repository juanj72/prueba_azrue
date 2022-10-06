from django.shortcuts import render

from .models import *
from crud.forms import *

# Create your views here.




def inicio(request):
    formulario=formulario_persona(request.POST or None)
    personas=persona.objects.all()

    if request.method=='POST':
        if formulario.is_valid():
            formulario.save()





    return render(request,"index.html",{"personas":personas,"formulario":formulario})