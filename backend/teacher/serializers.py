from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import Aula, Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    nome = serializers.CharField(max_length=100)

    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError('deve ter pelo menos três caracteres!')

        return value


class AulasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'