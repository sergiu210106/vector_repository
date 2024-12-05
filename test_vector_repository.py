import unittest
from myvector import MyVector
from vector_repository import VectorRepository  # Replace 'vector_repository' with the file name where the class is defined


class TestVectorRepository(unittest.TestCase):
    def setUp(self):
        """Set up a VectorRepository instance and sample vectors for testing."""
        self.repo = VectorRepository()
        self.vector1 = MyVector(name_id="v1", colour="r", type_=1, values=[1, 2, 3])
        self.vector2 = MyVector(name_id="v2", colour="g", type_=2, values=[4, 5, 6])
        self.vector3 = MyVector(name_id="v3", colour="b", type_=3, values=[7, 8, 9])
        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        self.repo.add(self.vector3)

    def test_add(self):
        self.setUp()
        """Test adding a vector to the repository."""
        new_vector = MyVector(name_id="v4", colour="y", type_=1, values=[10, 11, 12])
        self.repo.add(new_vector)
        self.assertIn(new_vector, self.repo.get_all_vectors())

    def test_get_all_vectors(self):
        """Test retrieving all vectors."""
        self.setUp()
        vectors = self.repo.get_all_vectors()
        self.assertEqual(len(vectors), 3)
        self.assertEqual(vectors[0].name_id, "v1")
        self.assertEqual(vectors[1].name_id, "v2")
        self.assertEqual(vectors[2].name_id, "v3")

    def test_get_vector_at_index(self):
        """Test retrieving a vector by index."""
        self.setUp()
        vector = self.repo.get_vector_at_index(1)
        self.assertEqual(vector.name_id, "v2")

    def test_update_by_index(self):
        """Test updating a vector by index."""
        self.setUp()
        updated_vector = self.repo.update_by_index(1, "v2_updated", "y", 2, [10, 20, 30])
        self.assertEqual(updated_vector.name_id, "v2_updated")
        self.assertEqual(updated_vector.colour, "y")
        self.assertEqual(updated_vector.type, 2)
        self.assertEqual(list(updated_vector.values), [10, 20, 30])

    def test_update_by_name_id(self):
        self.setUp()
        """Test updating a vector by its name_id."""
        updated_vector = self.repo.update_by_name_id("v1", "m", 3, [5, 5, 5])
        self.assertEqual(updated_vector.colour, "m")
        # self.assertEqual(updated_vector.type, 3)
        self.assertEqual(list(updated_vector.values), [5, 5, 5])

    def test_delete_by_index(self):
        """Test deleting a vector by index."""
        self.setUp()
        self.repo.delete_by_index(1)
        vectors = self.repo.get_all_vectors()
        self.assertEqual(len(vectors), 2)
        self.assertNotIn(self.vector2, vectors)

    def test_delete_by_name_id(self):
        """Test deleting a vector by its name_id."""
        self.setUp()
        self.repo.delete_by_name_id("v3")
        vectors = self.repo.get_all_vectors()
        self.assertEqual(len(vectors), 2)
        self.assertNotIn(self.vector3, vectors)

    def test_vectors_given_sum(self):
        """Test retrieving vectors by the sum of their values."""
        self.setUp()
        result = self.repo.vectors_given_sum(6)  # Sum of [1, 2, 3] is 6
        self.assertIn(self.vector1, result)
        self.assertNotIn(self.vector2, result)

    def test_delete_between_indices(self):
        """Test deleting vectors between specified indices."""
        self.setUp()
        self.repo.delete_between_indices(0, 1)
        vectors = self.repo.get_all_vectors()
        self.assertEqual(vectors[0].name_id, "v3")

    def test_update_color_by_name_id(self):
        """Test updating the colour of a vector by its name_id."""
        self.setUp()
        self.repo.update_color_by_name_id("v2", "b")
        vector = self.repo.get_vector_at_index(1)
        self.assertEqual(vector.colour, "b")

    def test_invalid_vector_sum(self):
        """Test handling invalid sum inputs in `vectors_given_sum`."""
        self.setUp()
        with self.assertRaises(TypeError):
            self.repo.vectors_given_sum("invalid_sum")

    def test_invalid_delete_between_indices(self):
        """Test invalid inputs for deleting between indices."""
        self.setUp()
        with self.assertRaises(IndexError):
            self.repo.delete_between_indices(2, 1)

    def test_invalid_update_color(self):
        """Test invalid inputs for updating color by name_id."""
        self.setUp()
        with self.assertRaises(ValueError):
            self.repo.update_color_by_name_id("v2", "invalid_color")


if __name__ == "__main__":
    unittest.main()
