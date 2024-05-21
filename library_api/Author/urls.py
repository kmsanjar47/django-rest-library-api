from django.urls import path
from rest_framework import routers
from Author.views import AuthorViewSet


router = routers.SimpleRouter()
router.register("author", AuthorViewSet, basename="authors")
print("Paths:", router.urls)

urlpatterns = router.urls
