from django.urls import path,include

from rest_framework import routers
from .views import StudentViewSet, ParentViewSet

router = routers.DefaultRouter()
router.register('student', StudentViewSet)
router.register('parent', ParentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
