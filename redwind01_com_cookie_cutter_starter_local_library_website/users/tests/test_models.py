from redwind01_com_cookie_cutter_starter_local_library_website.users.models import User


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
