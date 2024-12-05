import unittest
import numpy as np
from myvector import MyVector

class TestMyVector(unittest.TestCase):
    def setUp(self):
        """
        Set up test cases with reusable vector instances.
        """
        self.vector = MyVector(name_id="v1", colour="r", type_=1, values=[1, 2, 3])

    # Test initialization
    def test_initialization(self):
        self.assertEqual(self.vector.name_id, "v1")
        self.assertEqual(self.vector.colour, "r")
        self.assertEqual(self.vector.type, 1)
        np.testing.assert_array_equal(self.vector.values, np.array([1, 2, 3]))

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            MyVector(name_id=1, colour="x", type_=1, values=[1, 2, 3])  # Invalid colour
        with self.assertRaises(ValueError):
            MyVector(name_id=1, colour="r", type_=0, values=[1, 2, 3])  # Invalid type
        with self.assertRaises(ValueError):
            MyVector(name_id=1, colour="r", type_=1, values = "123")  # Invalid values

    # Test property getters and setters
    def test_name_id_setter(self):
        self.vector.name_id = "v2"
        self.assertEqual(self.vector.name_id, "v2")
        with self.assertRaises(ValueError):
            self.vector.name_id = None

    def test_colour_setter(self):
        self.vector.colour = "g"
        self.assertEqual(self.vector.colour, "g")
        with self.assertRaises(ValueError):
            self.vector.colour = "x"

    def test_type_setter(self):
        self.vector.type = 2
        self.assertEqual(self.vector.type, 2)
        with self.assertRaises(ValueError):
            self.vector.type = -1

    def test_values_setter(self):
        self.vector.values = [4, 5, 6]
        np.testing.assert_array_equal(self.vector.values, np.array([4, 5, 6]))
        with self.assertRaises(ValueError):
            self.vector.values = "invalid"

    # Test string representation
    def test_str_representation(self):
        expected_str = "MyVector(name_id=v1, colour='r', type=1, values=[1 2 3])"
        self.assertEqual(str(self.vector), expected_str)

    # Test add_scalar
    def test_add_scalar(self):
        result = self.vector.add_scalar(2)
        np.testing.assert_array_equal(result, np.array([3, 4, 5]))
        with self.assertRaises(ValueError):
            self.vector.add_scalar("invalid")

    # Test add
    def test_add(self):
        result = self.vector.add([1, 1, 1])
        np.testing.assert_array_equal(result, np.array([2, 3, 4]))
        with self.assertRaises(ValueError):
            self.vector.add([1, 2])  # Length mismatch
        with self.assertRaises(ValueError):
            self.vector.add(["invalid", 2, 3])  # Invalid type

    # Test subtract
    def test_subtract(self):
        result = self.vector.subtract([1, 1, 1])
        np.testing.assert_array_equal(result, np.array([0, 1, 2]))
        with self.assertRaises(ValueError):
            self.vector.subtract([1, 2])  # Length mismatch
        with self.assertRaises(ValueError):
            self.vector.subtract(["invalid", 2, 3])  # Invalid type

    # Test multiplication
    def test_multiplication(self):
        result = self.vector.multiplication([2, 2, 2])
        self.assertEqual(result, 12)  # Dot product
        with self.assertRaises(ValueError):
            self.vector.multiplication([1, 2])  # Length mismatch

    # Test sum_of_values
    def test_sum_of_values(self):
        self.assertEqual(self.vector.sum_of_values(), 6)

    # Test product_of_values
    def test_product_of_values(self):
        self.assertEqual(self.vector.product_of_values(), 6)

    # Test average_of_values
    def test_average_of_values(self):
        self.assertEqual(self.vector.average_of_values(), 2)

    # Test minimum_of_values
    def test_minimum_of_values(self):
        self.assertEqual(self.vector.minimum_of_values(), 1)

    # Test maximum_of_values
    def test_maximum_of_values(self):
        self.assertEqual(self.vector.maximum_of_values(), 3)

if __name__ == "__main__":
    unittest.main()
