from django.shortcuts import render

from .models import *

# Create your views here.




def inicio(request):
    personas=persona.objects.all()




    return render(request,"./index.html",{"personas":personas})