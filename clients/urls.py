from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .api.v1.viewsets import ClientViewSet


client_detail = ClientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('clients/', client_detail, name='client-detail')
])
