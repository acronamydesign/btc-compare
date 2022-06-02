from unittest import TestCase
from arbitrage.credentials import AuthManager


class TestAuthManager(TestCase):
    def test_load_credentials(self):
        credentials = AuthManager().load_credentials()
        assert isinstance(credentials, bool) or isinstance(credentials, dict)

    def test_create_credentials(self):
        auth = AuthManager()
        auth.delete_credentials()
        auth.create_credentials()
        credentials = auth.load_credentials()
        assert isinstance(credentials, dict)