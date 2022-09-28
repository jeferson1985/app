from re import M
from django.shortcuts import render
from django.http import JsonResponse

from .models import Medicamentos

from rest_framework.viewsets import ModelViewSet

from .serializers import MedicamentoSerializer


class MedicamentosViewSet(ModelViewSet):
    queryset = Medicamentos.objects.all()
    serializer_class = MedicamentoSerializer
        