from unittest.mock import Mock
import pytest
from django.contrib.auth import get_user_model


# Method to test
def user_has_perm(user, perm: str):
    return perm in user.get_all_permissions()


@pytest.fixture
def user_with_perm():
    # Create a user without saving it to the DB
    User = get_user_model()
    user = User(username='a_user')
    # Mock get_all_permissions to avoid a database access
    user.get_all_permissions = Mock(return_value={'admin.add_logentry'})
    return user


def test_user_can_add_log_entry(user_with_perm):
    assert user_has_perm(user_with_perm, 'admin.add_logentry')


def test_user_cant_delete_log_entry(user_with_perm):
    assert not user_has_perm(user_with_perm, 'admin.delete_logentry')
