from rest_framework import routers

from .api.v1.viewsets import ClientViewSet


V1_ROUTER = routers.DefaultRouter()
V1_ROUTER.register(r'clients', ClientViewSet)

urlpatterns = V1_ROUTER.urls
