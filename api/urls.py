from xml.etree.ElementInclude import include
from django.urls import path,include
from rest_framework import routers
from .views import PersonViewSet

router = routers.DefaultRouter()
router.register ('person', PersonViewSet)

urlpatterns = [
    path('', include(router.urls))
]
