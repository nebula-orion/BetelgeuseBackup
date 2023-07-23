# Local imports
from betelgeuse.main import main


def test_main():
    assert main() == "Hello, world!"
