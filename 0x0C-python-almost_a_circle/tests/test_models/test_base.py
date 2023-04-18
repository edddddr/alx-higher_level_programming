#!/usr/bin/python3

"""Tests that a base class creates an instance of a base object correctly"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestBaseClass(unittest.TestCase):
    """tests that a base class creates an object
    properly
    """

    def test_create_base_obj(self):
        """check that a base object gets created"""
        new_obj = Base()
        new_obj_2 = Base(68)
        self.assertTrue(new_obj)
        self.assertTrue(new_obj_2)

    def test_instance_is_base(self):
        """check that the instance is of ``Base`` type"""
        new_obj = Base()
        new_obj_2 = Base(32)
        self.assertTrue(type(new_obj) == Base)
        self.assertTrue(type(new_obj_2) == Base)
        self.assertFalse(type(new_obj) == int)
        self.assertFalse(type(new_obj_2) == dict)
    
    def test_check_base_id(self):
        """check that the id of a base instance is correct"""
        new_obj = Base()
        new_obj_2 = Base(68)
        new_obj_3 = Base()
        self.assertEqual(new_obj.id, 1)
        self.assertEqual(new_obj_2.id, 68)
        self.assertEqual(new_obj_3.id, 2)

    def test_to_json_string(self):
        """checks that a dictionary gets converted to a json string"""
        new_obj = Base()
        new_obj_2 = Rectangle(6, 4)
        obj = new_obj.to_json_string([new_obj_2.to_dictionary()])
        self.assertEqual(type(obj), str)
        with self.assertRaises(TypeError):
            new_obj.to_json_string(new_obj_2.to_dictionary())
        with self.assertRaises(TypeError):
            new_obj.to_json_string([{"key": "value"}, "string", 123])
        with self.assertRaises(TypeError):
            new_obj.to_json_string(str(new_obj_2.to_dictionary()))
        self.assertEqual(new_obj.to_json_string([]), '[]')
        self.assertEqual(new_obj.to_json_string(None), '[]')
        self.assertIsNotNone(new_obj.to_json_string(None))
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_save_to_file(self):
        """checks that rectangle and squae instances are saved to files"""
        new_obj = Rectangle(10, 5)
        new_obj_2 = Square(5)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([new_obj, 7])
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([new_obj, new_obj_2])
        self.assertIsNotNone(Base.save_to_file.__doc__)

    def test_from_json_string(self):
        """checks that a list object is returned
        from a json strin representation"""
        new_obj = Rectangle(10, 5)
        new_obj_2 = Square(5)
        obj = new_obj.to_json_string([new_obj_2.to_dictionary()])
        list_obj = Rectangle.from_json_string(obj)
        self.assertIsNotNone(list_obj)
        self.assertEqual(type(list_obj), list)
        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertIsNotNone(Base.from_json_string.__doc__)

    def test_create(self):
        """checks that rectangle and square instances are created"""
        obj_1 = Square(20)
        obj_1_dict = obj_1.to_dictionary()
        obj_2 = Square.create(**obj_1_dict)
        self.assertFalse(obj_1 is obj_2)

    def test_load_from_file(self):
        """checks that an instance is loaded from a file"""
        self.assertIsNotNone(Base.load_from_file.__doc__)


if __name__ == "__main__":
    unittest.main()
