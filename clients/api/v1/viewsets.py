from rest_framework.viewsets import ModelViewSet

from clients.api.v1.serializers import ClientSerializer
from clients.models import Client


class ClientViewSet(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
