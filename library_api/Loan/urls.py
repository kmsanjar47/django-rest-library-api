from rest_framework import routers
from Loan.views import LoanViewSet

router = routers.SimpleRouter()
router.register("loan", viewset=LoanViewSet, basename="loan")


urlpatterns = router.urls
