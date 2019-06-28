from rest_framework import routers
from links.viewsets import LinkViewSet
router = routers.DefaultRouter()
router.register(r'link', LinkViewSet)