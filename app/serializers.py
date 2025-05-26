from rest_framework import serializers
from .models import Sensores , Ambientes , Historico

class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        fields = '__all__'

    # Mensagem de erro para caso o usuario crie sensores com dados errado
    def is_valid(self, *, raise_exception=False):
        try:
            super().is_valid(raise_exception=raise_exception)
            super().save()
        except Exception as e:
            raise serializers.ValidationError({"Erro ao criar sensores, verifique os dados enviados."})

class AmbientesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        fields = '__all__'
    # Mensagem de erro para caso o usuario crie o ambiente com dados errado
    def is_valid(self, *, raise_exception=False):
        try:
            super().is_valid(raise_exception=raise_exception)
            super().save()
        except Exception as e:
            raise serializers.ValidationError({"Erro ao criar Ambientes, verifique os dados enviados."})

class HistoricoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'
    # Mensagem de erro para caso o usuario crie o historico com dados errado
    def is_valid(self, *, raise_exception=False):
        try:
            super().is_valid(raise_exception=raise_exception)
            super().save()
        except Exception as e:
            raise serializers.ValidationError({"Erro ao criar historico, verifique os dados enviados."})
