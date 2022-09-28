from rest_framework.serializers import ModelSerializer

from .models import Medicamentos

class MedicamentoSerializer(ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = ['name', 'price', 'indications', 'againstIndications', 'adverseReactions', 'precautions',]
        