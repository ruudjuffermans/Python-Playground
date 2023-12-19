"""
This module contains test functions for demonstrating unit testing in Python.

The tests here are designed to showcase how assertions work in a test environment,
using Python's built-in 'assert' statement.
"""


def test_failing():
    """
    Test to demonstrate a failing assertion.

    This function tests the assertion that two tuples are equal.
    However, the tuples here are intentionally mismatched to demonstrate
    a failing test case in a unit testing scenario.

    Returns:
        None: This function is designed to assert a condition and does not return a value.
    """
    assert (1, 2, 3) == (3, 2, 1)
