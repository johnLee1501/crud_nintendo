from rest_framework import serializers

from nintendo.models import NintendoModel


class NintendoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NintendoModel
        fields = '__all__'
