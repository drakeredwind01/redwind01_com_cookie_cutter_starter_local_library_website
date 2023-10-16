from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "redwind01_com_cookie_cutter_starter_local_library_website.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import redwind01_com_cookie_cutter_starter_local_library_website.users.signals  # noqa: F401
        except ImportError:
            pass
