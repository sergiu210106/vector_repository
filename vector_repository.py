from operator import index
from random import *
import matplotlib.pyplot as plt
from myvector import MyVector

class VectorRepository:
    def __init__(self):
        '''
        Constructor for the vector repository
        '''
        self.__vectors = []
        self.__size = 0

    def add(self, vector):
        '''
        function that adds a vector to the vector repository
        :param vector:
        :return:
        '''
        for v in self.__vectors:
            if v.name_id == vector.name_id:
                return self.__vectors
        self.__vectors.append(vector)
        self.__size += 1

        return self.__vectors

    def get_all_vectors(self):
        '''
        function that returns all the vectors in the vector repository
        :return: list[MyVector]
        '''
        return self.__vectors

    def get_vector_at_index(self, index):
        '''
        function that returns the vector at the given index
        :param index: int
        :return: MyVector
        '''

        return self.__vectors[index]

    def update_by_index(self, index, name_id, colour, type_, values):
        '''
        function that updates the vector at the given index
        :param index: int
        :param name_id: str|int
        :param colour: str
        :param type_: int
        :param values: list[int|float]
        :return: MyVector
        '''
        self.__vectors[index] = MyVector(name_id, colour, type_, values)
        return self.__vectors[index]

    def update_by_name_id(self, name_id, colour, type_, values):
        '''
        function that updates the vector by name_id
        :param name_id: str|int
        :param colour: str
        :param type_: int
        :param values: list[int|float]
        :return: MyVector
        '''
        for vector in self.__vectors:
            if vector.name_id == name_id:
                vector.colour = colour
                vector.type_ = type_
                vector.values = values
                return vector

        return None
    def delete_by_index(self, index):
        '''
        function that deletes the vector at the given index
        :param index: int
        :return: list[MyVector]
        '''

        del self.__vectors[index]
        return self.__vectors[index]

    def delete_by_name_id(self, name_id):
        '''
        function that deletes the vector by name_id
        :param name_id: str|int
        :return: list[MyVector]
        '''

        for index in range(self.__size - 1, -1, -1):
            if self.__vectors[index].name_id == name_id:
                del self.__vectors[index]

        return self.__vectors

    def plot(self):

        markers = {1 : 'o', 2 : 's', 3 : '^'}
        default_marker = 'D'

        plt.figure(figsize=(8,6))

        for vector in self.__vectors:
            values = vector.values
            colour = vector.colour
            type_ = vector.type
            marker = markers.get(type_, default_marker)

            plt.plot(
                range(len(values)),
                values,
                color = colour,
                marker = marker,
                label = f"ID : {vector.name_id} (Type: {vector.type})"
            )

        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title("Vector plot by type and color")
        plt.legend()
        plt.show()

    # extra : problems 11, 19, 22

    # 11
    def vectors_given_sum(self, sum):
        '''
        function that returns the vectors given the sum of the values in the vector.
        :param sum: int|float
        :return: list[MyVector]
        '''
        if not isinstance(sum, (int, float)):
            raise TypeError("the sum must be int or float")
        else:
            return [vector for vector in self.__vectors if vector.sum_of_values() == sum]

    # 19
    def delete_between_indices(self, start, end):
        '''
        function that deletes the vectors between the given indices.
        :param start: int
        :param end: int
        :return: list[MyVector]
        '''
        if not start <= end or not isinstance(start, int) or not isinstance(end, int):
            raise IndexError("start and end must be integers and start <= end")
        else:
            self.__vectors = self.__vectors[:start] + self.__vectors[end+1:]
            return self.__vectors
    # 22
    def update_color_by_name_id(self, name_id, colour):
        '''
        function that updates the vector's colour by name_id
        :param name_id: str|int
        :param colour: str - colour must be 'r', 'g', 'b', 'y', or 'm'.
        :return:
        '''
        if not isinstance(name_id, (str, int)):
            raise ValueError("name_id must be a string or an integer.")
        if colour not in ['r', 'g', 'b', 'y', 'm']:
            raise ValueError("colour must be 'r', 'g', 'b', 'y', or 'm'.")

        for vector in self.__vectors:
            if vector.name_id == name_id:
                vector.colour = colour
        return self.__vectors

    def randomize(self, length):
        '''
        function that adds 10 random vectors to the vector list.
        :param length: int
        :return: list[MyVector]
        '''
        NAME_IDS = [str(number) for number in range(10)]
        VALID_COLORS = ['r', 'g', 'b', 'y', 'm']
        TYPE_RANGE = range(1, 10)
        VALUES_LEN_RANGE = range(1, 10)
        VALUE_RANGE = range(1, 10)

        vectors = []
        i = 0
        while len(vectors) < length:
            name_id = len(vectors)
            colour = choice(VALID_COLORS)
            type_ = choice(TYPE_RANGE)
            values = [choice(VALUE_RANGE) for _ in range(choice(VALUES_LEN_RANGE))]

            if MyVector(name_id, colour, type_, values) not in vectors:
                self.__vectors.append(MyVector(name_id, colour, type_, values))
                vectors.append(MyVector(name_id, colour, type_, values))

        return vectors





