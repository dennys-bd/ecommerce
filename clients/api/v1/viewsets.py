from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from clients.models import Client

from .serializers import ClientSerializer


class ClientViewSet(DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_object(self):
        return self.request.user
