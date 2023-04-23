import logging

from ...src.hello_world import get_hello_world
from ...src.utilities import logger

logger.setLevel(logging.INFO)


class TestClass:
    def test_hello_world(self):
        expected = "Hello World"
        actual = get_hello_world()
        assert actual == expected
