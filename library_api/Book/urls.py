from rest_framework import routers
from Book.views import BookViewSet


router = routers.SimpleRouter()
router.register("book", viewset=BookViewSet, basename="book")
print("Book", router.urls)

urlpatterns = router.urls
