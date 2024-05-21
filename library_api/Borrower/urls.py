from rest_framework import routers
from Borrower.views import BorrowerViewSet

router = routers.SimpleRouter()
router.register("borrower", viewset=BorrowerViewSet, basename="borrower")


urlpatterns = router.urls
