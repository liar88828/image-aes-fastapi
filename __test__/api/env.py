import unittest

from key import settings


def test_environment():
    assert settings.REFRESH_TOKEN_EXPIRE_DAY == 30


if __name__ == '__main__':
    unittest.main()
