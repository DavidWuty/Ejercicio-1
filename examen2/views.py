from django.shortcuts import render
from rest_framework import viewsets

from .models import Mascota
from .serializer import MascotaSerializer

# Create your views here.

class MascotaViewset(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer