import json
import pytest
from baker3000 import Machine

def test_load_existing_json_file():
    baker3000 = Machine()
    assert baker3000.load_ingredients() == {
    "eggs": 6,
    "milk": 600,
    "butter": 600,
    "flour": 600,
    "sugar": 600,
    "chocolate": 600,
    "vanilla": 10,
    "water": 300,
    "soap": 50
}