import pytest

from redwind01_com_cookie_cutter_starter_local_library_website.users.models import User
from redwind01_com_cookie_cutter_starter_local_library_website.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
