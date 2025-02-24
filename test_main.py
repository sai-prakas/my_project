# test_main.py

from utils import greet

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Python") == "Hello, Python!"
