import numpy as np

import vector_repository
from myvector import MyVector
from vector_repository import VectorRepository

def options():
    print("Please enter one of the following options:")
    print("1. Add a vector to the repository.")
    print("2. Get all vectors from the repository.")
    print("3. Get a vector at a given index.")
    print("4. Update a vector at a given index.")
    print("5. Update a vector identified by name_id.")
    print("6. Delete a vector by index.")
    print("7. Delete a vector by name_id.")
    print("8. Plot all vectors in a chart based on type and colour. Type should be one of the following: 1 - circle, 2 - square, 3 - triangle, any other value - diamond")
    print("9. Get the list of vectors having a given sum of elements. (Extra # 11)")
    print("10. Delete all vectors between two indices. (Extra # 19)")
    print("11. Update the colour by name_id.(Extra # 22")
    print("12. QUIT.")


def ui():
    repo = VectorRepository()
    repo.randomize(10)

    while True:

        options()
        option = input("Enter your choice: ")
        match option:
            case '1':
                name_id = input("Enter the name_id of vector: ")
                if not isinstance(name_id, (str, int)):
                    raise ValueError("name_id must be a string or an integer.")

                colour = input("Enter the colour of vector: ")
                if colour not in ['r', 'g', 'b', 'y', 'm']:
                    raise ValueError("colour must be 'r', 'g', 'b', 'y', or 'm'.")

                try:
                    type_ = int(input("Enter the type of the vector: "))
                    if type_ < 1:
                        raise ValueError("The type must be a positive integer greater than or equal to 1.")
                except ValueError:
                    raise ValueError("The type must be a positive integer greater than or equal to 1.")

                values = input("Enter the values of vector separated by spaces: ").split()
                try:
                    values = [int(value) for value in values]
                except ValueError:
                    raise ValueError("values must be a float or an integer.")

                vector = MyVector(name_id, colour, type_, values)
                repo.add(vector)
            case '2':
                for vector in repo.get_all_vectors():
                    print(vector)
            case '3':
                n = len(repo.get_all_vectors())
                try:
                    index = int(input("Enter the index of vector: "))

                    if not (0 <= index <= n - 1):
                        raise IndexError("index must be between 0 and " + str(n - 1))

                    print(repo.get_vector_at_index(index))
                except ValueError:
                    raise ValueError("index must be an integer between 0 and " + str(n - 1))
            case '4':
                n = len(repo.get_all_vectors())
                try:
                    index = int(input("Enter the index: "))

                    if not (0 <= index <= n - 1):
                        raise IndexError("index must be between 0 and " + str(n - 1))

                except ValueError:
                    raise ValueError("index must be an integer between 0 and " + str(n - 1))

                name_id = input("Enter the name_id of the vector: ")
                if not isinstance(name_id, (str, int)):
                    raise ValueError("name_id must be a string or an integer.")

                colour = input("Enter the colour of vector: ")
                if colour not in ['r', 'g', 'b', 'y', 'm']:
                    raise ValueError("colour must be 'r', 'g', 'b', 'y', or 'm'.")

                try:
                    type_ = int(input("Enter the type of vector: "))
                    if type_ < 1:
                        raise ValueError("The type must be a positive integer greater than or equal to 1.")
                except ValueError:
                    raise ValueError("The type must be a positive integer greater than or equal to 1.")

                values = input("Enter the values of vector separated by spaces: ").split()
                try:
                    values = [float(value) for value in values]
                except ValueError:
                    raise ValueError("values must be a float or an integer.")

                repo.update_by_index(index, name_id, colour, type_, np.array(values))

            case '5':
                name_id = input("Enter the name_id of the vector: ")
                if not isinstance(name_id, (str, int)):
                    raise ValueError("name_id must be a string or an integer.")

                colour = input("Enter the colour of vector: ")
                if colour not in ['r', 'g', 'b', 'y', 'm']:
                    raise ValueError("colour must be 'r', 'g', 'b', 'y', or 'm'.")

                try:
                    type_ = int(input("Enter the type of vector: "))
                    if type_ < 1:
                        raise ValueError("The type must be a positive integer greater than or equal to 1.")
                except ValueError:
                    raise ValueError("The type must be a positive integer greater than or equal to 1.")

                values = input("Enter the values of vector separated by spaces: ").split()
                try:
                    values = [float(value) for value in values]
                except ValueError:
                    raise ValueError("values must be a float or an integer.")

                repo.update_by_name_id(name_id, colour, type_, np.array(values))
            case '6':
                n = len(repo.get_all_vectors())
                try:
                    index = int(input("Enter the index: "))

                    if not (0 <= index <= n - 1):
                        raise IndexError("index must be between 0 and " + str(n - 1))

                except ValueError:
                    raise ValueError("index must be an integer between 0 and " + str(n - 1))

                repo.delete_by_index(index)

            case '7':
                name_id = input("Enter the name_id of the vector: ")
                if not isinstance(name_id, (str, int)):
                    raise ValueError("name_id must be a string or an integer.")

                repo.delete_by_name_id(name_id)
            case '8':
                repo.plot()
            case '9':
                sum = input("Enter the sum of the vector: ")

                for vector in repo.vectors_given_sum(sum):
                    print(vector)

            case '10':
                start = input("Enter the start index for deletion: ")
                end = input("Enter the end index for deletion: ")

                repo.delete_between_indices(start, end)
            case '11':
                name_id = input("Enter the name_id of the vector: ")
                if not isinstance(name_id, (str, int)):
                    raise ValueError("name_id must be a string or an integer.")
                colour = input("Enter the colour of vector: ")
                if colour not in ['r', 'g', 'b', 'y', 'm']:
                    raise ValueError("colour must be 'r', 'g', 'b', 'y', or 'm'.")

                repo.update_color_by_name_id(name_id, colour)
            case '12':
                break