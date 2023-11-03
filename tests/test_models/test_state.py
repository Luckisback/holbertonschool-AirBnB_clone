#!/usr/bin/python3
"""Test for State class"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_default_name_attribute(self):
        """Test the default name attribute of a State instance."""
        state = State()
        self.assertEqual(state.name, "")

    def test_instance_creation(self):
        """Test if a State instance can be created."""
        state = State()
        self.assertIsInstance(state, State)

    def test_name_attribute_type(self):
        """Test the data type of the name attribute of a State instance."""
        state = State()
        self.assertIsInstance(state.name, str)

if __name__ == '__main__':
    unittest.main()
