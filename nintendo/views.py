from rest_framework.viewsets import ModelViewSet

from nintendo.models import NintendoModel
from nintendo.serializers import NintendoSerializer


class NintendoViewSet(ModelViewSet):
    queryset = NintendoModel.objects.all()
    serializer_class = NintendoSerializer
