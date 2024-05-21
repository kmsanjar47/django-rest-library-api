from rest_framework import routers
from Category.views import CategoryViewSet


router = routers.SimpleRouter()
router.register("category", viewset=CategoryViewSet, basename="category")


urlpatterns = router.urls
