from rest_framework import routers
from Branch.views import BranchViewset


router = routers.SimpleRouter()
router.register("branch", viewset=BranchViewset, basename="branch")


urlpatterns = router.urls
