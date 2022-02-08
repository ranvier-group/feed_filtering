import itertools

import pytest

import filtering

to = [
    ({"to": "herbajerba"}, False),
    ({"to": 0}, False),
    ({"to": 1}, False),
    ({"to": "0x01"}, False),
    ({"to": "0x1"}, True) 
]

from_or_to = [
    ({"to": "0x0", "from": "0x2"}, True),
    ({"to": "0x0", "from": "0x1"}, False),
    ({"to": "0x2", "from": "0x0"}, False),
    ({"to": "0x1", "from": "0x2"}, True),
    ({"to": "0x0", "from": "0x2"}, True)
]

from_or_to_and_input = [
    ({"to": "0x1", "from": "", "input": "0x0"}, True),
    ({"to": "", "from": "0x2", "input": "0x0"}, True),
    ({"to": "0x1", "from": "", "input": "0x1"}, False),
    ({"to": "0x1", "from": "", "input": "0x0"}, True)
]

from_or_to_and_input_or_method_id = [
    ({"to": "0x1", "from": "", "input": "0x12345678"}, True),
    ({"to": "", "from": "0x2", "input": "0x12345678abc"}, True),
    ({"to": "0x1", "from": "0x0", "input": "0x123x5678"}, False)
]

def test_simple_to():
    """'to'"""
    filter = filtering.Filter(
        {"to": "0x1"}
    )

    for case in to:
        assert filtering.filter_tx(case[0], [filter]) == case[1]


def test_from_or_to():
    """'from' OR 'to'"""
    filter = filtering.Filter(
        {"to": "0x1", "from": "0x2"}
    )

    for case in from_or_to:
        assert filtering.filter_tx(case[0], [filter]) == case[1]


def test_from_or_to_and_input():
    """(from OR to) AND input"""
    f1 = filtering.Filter({"to": "0x1", "from": "0x2"})
    f2 = filtering.Filter({"input": "0x0"})

    for case in from_or_to_and_input:
        assert filtering.filter_tx(case[0], [[f1, f2]]) == case[1]

def test_from_or_to_and_input_or_method_id():
    """((from OR to) AND input) OR method_id"""
    f1 = filtering.Filter({"to": "0x1", "from": "0x2"})
    f2 = filtering.Filter({"input": "0x0"})
    f3 = filtering.Filter({"method_id": "12345678"})
    
    for case in itertools.chain(from_or_to_and_input, from_or_to_and_input_or_method_id):
        assert filtering.filter_tx(case[0], [[f1, f2], f3]) == case[1]
