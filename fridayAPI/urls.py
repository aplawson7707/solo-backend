from rest_framework import routers
from fridayAPI.views import (
    ShoppingListItemViewSet,
    TestViewSet,
)


router = routers.DefaultRouter()

router.register('test', TestViewSet)
router.register('shopping_list', ShoppingListItemViewSet)