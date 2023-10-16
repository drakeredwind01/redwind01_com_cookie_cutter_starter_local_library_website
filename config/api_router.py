from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from redwind01_com_cookie_cutter_starter_local_library_website.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
