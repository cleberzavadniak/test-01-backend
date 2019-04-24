import pytest


def test_load_database(authenticator):
    assert hasattr(authenticator, 'db')


def test_hash_password(authenticator, password, hashed_password):
    assert authenticator.hash_password(password) == hashed_password


def test_check_password(authenticator, password, hashed_password):
    assert authenticator.check_password(password, hashed_password) is True


def test_authenticate_existent_user(authenticator, username, password):
    value = authenticator.authenticate(username, password)
    # {'id': 1, 'username': 'test@example.com'}
    assert 'id' in value
    assert value['id'] == 1
    assert 'username' in value
    assert value['username'] == username


def test_authenticate_inexistent_user(authenticator):
    with pytest.raises(Exception):
        authenticator.authenticate('inexistent-user', 'wrong-password')


def test_generate_token(authenticator):
    token = authenticator.generate_token()
    assert '-' not in token
    assert len(token) > 20


def test_sign_up(empty_authenticator, password, hashed_password):
    value = empty_authenticator.sign_up('new-user', password)
    assert 'id' in value
    assert value['id'] == 1
    assert 'token' in value
    assert len(value['token']) > 20
    assert '-' not in value['token']

    table = empty_authenticator.mocked_table
    assert table.insert.call_count == 1
    first_call = table.insert.call_args_list[0]
    call_args = first_call[0]
    first_arg = call_args[0]

    assert 'username' in first_arg
    assert first_arg['username'] == 'new-user'

    assert 'password' in first_arg
    assert first_arg['password'] == hashed_password


def test_sign_up_with_existing_user(authenticator, password):
    with pytest.raises(Exception) as ex:
        authenticator.sign_up('new-user', password)

    assert 'already exists' in str(ex)
