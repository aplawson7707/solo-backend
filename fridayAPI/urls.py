from rest_framework import routers
from fridayAPI.views import TestViewSet


router = routers.DefaultRouter()

router.register('test', TestViewSet)
