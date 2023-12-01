from rest_framework.routers import SimpleRouter
from general.api.views import ItemViewSet

router = SimpleRouter()
router.register(r'items', ItemViewSet, basename='items')

urlpatterns = router.urls
