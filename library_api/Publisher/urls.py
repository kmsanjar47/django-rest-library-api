from rest_framework import routers
from Publisher.views import PublisherViewSet


router = routers.SimpleRouter()
router.register("publisher", viewset=PublisherViewSet, basename="publisher")


urlpatterns = router.urls
