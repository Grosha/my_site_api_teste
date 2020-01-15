import pytest

from settings.services import my_site
from settings.user import User


class TestAuthorizeUser(object):

    @pytest.mark.parametrize(
        'username, password, status_code',
        [
            {'Alan', 'dog', 404},
            {'Alan', '', 404},
            {'Alan', None, 404},
            {None, 'dog', 404},
        ]
    )
    def test_authorize_user_negative(self, username, password, status_code):
        user = User(username=username, password=password)
        response = my_site.authorize(user=user.credential)

        assert response.get('status') == status_code, 'Incorrect status code for authorization'
        assert response.get('message') == 'Incorrect credential information', 'Incorrect status code for authorization'

    def test_authorize_new_user(self):
        user = User(username='Devid', password='Beckham')
        response = my_site.authorize(user=user.credential)

        assert response.get('status') == 200, 'Incorrect status code for authorization new user'
