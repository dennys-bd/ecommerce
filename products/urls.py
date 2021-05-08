from rest_framework import routers

from .api.v1.viewsets import ProductViewSet


V1_ROUTER = routers.DefaultRouter()
V1_ROUTER.register(r'products', ProductViewSet, basename='product')

urlpatterns = V1_ROUTER.urls
