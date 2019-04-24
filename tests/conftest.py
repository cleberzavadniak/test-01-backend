from unittest.mock import Mock
import pytest

from authenticator.auth import Authenticator


@pytest.fixture
def username():
    return 'test@example.com'


@pytest.fixture
def password():
    return 'test-password'


@pytest.fixture
def hashed_password():
    return '$p5k2$$testsalt$RsPkXkfJ0oJ0iD4aWtI17R1VEGAQLH.C'


@pytest.fixture
def salt():
    return 'testsalt'


@pytest.fixture
def authenticator(salt, username, hashed_password):
    MockedFind = Mock(return_value=[{
        'id': 1,
        'username': username,
        'password': hashed_password,
    }])
    MockedTable = Mock(find=MockedFind)
    MockedDatabase = {'users': MockedTable}

    class MockedAuthenticator(Authenticator):
        def load_database(self, *args, **kwargs):
            self.db = MockedDatabase

    MockedAuthenticator.mocked_find = MockedFind
    MockedAuthenticator.mocked_table = MockedTable
    MockedAuthenticator.mocked_database = MockedDatabase

    return MockedAuthenticator(salt)


@pytest.fixture
def empty_authenticator(salt, username, hashed_password):
    MockedFind = Mock(return_value=[])
    MockedFindOne = Mock(return_value=None)
    MockedInsert = Mock(return_value=1)
    MockedTable = Mock(find=MockedFind, find_one=MockedFindOne, insert=MockedInsert)
    MockedDatabase = {'users': MockedTable}

    class MockedAuthenticator(Authenticator):
        def load_database(self, *args, **kwargs):
            self.db = MockedDatabase

    MockedAuthenticator.mocked_find = MockedFind
    MockedAuthenticator.mocked_table = MockedTable
    MockedAuthenticator.mocked_database = MockedDatabase

    return MockedAuthenticator(salt)
