#!/usr/bin/env python3
"""
A module for testing the utils module.
"""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """
        Test that access_nested_map returns the correct value.

        Parameters
        ----------
        nested_map : Dict
            The nested map to access.
        path : Tuple[str]
            The path of keys to access the value.
        expected : Union[Dict, int]
            The expected value.

        Returns
        -------
        None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple
                                         [str], exception: Exception) -> None:
        """
        Test that access_nested_map raises the correct exception.

        Parameters
        ----------
        nested_map : Dict
            The nested map to access.
        path : Tuple[str]
            The path of keys to access the value.
        exception : Exception
            The expected exception.

        Returns
        -------
        None
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test suite for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test that get_json returns the correct JSON data.

        Parameters
        ----------
        test_url : str
            The URL to request JSON data from.
        test_payload : Dict
            The expected JSON payload.

        Returns
        -------
        None
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test suite for the memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Test that the memoize decorator caches the result of the method.

        Returns
        -------
        None
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
