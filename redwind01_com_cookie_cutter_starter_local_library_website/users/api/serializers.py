from django.contrib.auth import get_user_model
from rest_framework import serializers

from redwind01_com_cookie_cutter_starter_local_library_website.users.models import User as UserType


User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }
