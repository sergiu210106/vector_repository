import numpy as np
class MyVector:
    def __init__(self, name_id, colour, type_, values):
        """
        Initializes a MyVector object.

        Args:
            name_id (str or int): The identifier for the vector.
            colour (str): The color of the vector ('r', 'g', 'b', 'y', 'm').
            type_ (int): The type of the vector, must be a positive integer >= 1.
            values (list): A list of numbers representing the vector's values.

        Raises:
            ValueError: If inputs do not meet the required constraints.
        """
        if not isinstance(name_id, (str, int)):
            raise ValueError("name_id must be a string or an integer.")
        else:
            self.__name_id = name_id

        if colour not in ['r', 'g', 'b', 'y', 'm']:
            raise ValueError("colour must be 'r', 'g', 'b', 'y', or 'm'.")
        else:
            self.__colour = colour
        if not isinstance(type_, int) or type_ < 1:
            raise ValueError("type must be a positive integer greater than or equal to 1.")
        else:
            self.__type = type_
        if not isinstance(values, list) or not all(isinstance(v, (int, float)) for v in values):
            raise ValueError("values must be a list of numbers (int or float).")
        else:
            self.__values = np.array(values)

    # Getter and setter for name_id
    @property
    def name_id(self):
        return self.__name_id

    @name_id.setter
    def name_id(self, value):
        if not isinstance(value, (str, int)):
            raise ValueError("name_id must be a string or an integer.")
        self.__name_id = value

    # Getter and setter for colour
    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, value):
        if value not in ['r', 'g', 'b', 'y', 'm']:
            raise ValueError("colour must be 'r', 'g', 'b', 'y', or 'm'.")
        self.__colour = value

    # Getter and setter for type
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("type must be a positive integer greater than or equal to 1.")
        self.__type = value

    # Getter and setter for values
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        if not isinstance(value, list) or not all(isinstance(v, (int, float)) for v in value):
            raise ValueError("values must be a list of numbers (int or float).")
        self.__values = np.array(value)

    def __str__(self):
        """
        Provides a string representation of the vector.

        Returns:
            str: A string representation of the vector.
        """
        return f"MyVector(name_id={self.__name_id}, colour='{self.__colour}', type={self.__type}, values={self.__values})"

    def __repr__(self):
        """
        Provides a developer-friendly representation of the vector.

        Returns:
            str: A detailed representation of the vector.
        """
        return self.__str__()


    def add_scalar(self, scalar : int|float):
        '''
        function that adds a scalar value to the vector.
        :param scalar: int|float
        :return: list[int|float]
        '''
        if not isinstance(scalar, (int, float)):
            raise ValueError("scalar must be an integer or float.")
        else:
            return np.add(self.__values, scalar)

    def add(self, values : list['int|float']):
        '''
        function that adds a list of values to the vector.
        :param values: list[int|float]
        :return: np.array
        '''
        if len(values) != len(self.__values):
            raise ValueError("values must have the same length as the vector.")
        elif not all([isinstance(value, (int, float)) for value in values]):
            raise ValueError("values must be a list of numbers (int or float).")
        else:
            return np.array(values) + self.__values

    def subtract(self, values : list['int|float']):
        '''
        function that subtracts a list of values from the vector.
        :param values: list[int|float]
        :return: list[int|float]
        '''
        if len(values) != len(self.__values):
            raise ValueError("values must have the same length as the vector.")
        elif not all([isinstance(value, (int, float)) for value in values]):
            raise ValueError("values must be a list of numbers (int or float).")
        else:
            return self.__values - np.array(values)

    def multiplication(self, values : list['int|float']):
        '''
        function that multiplies a list of values and the vector.
        :param values: list[int|float]
        :return: int|float
        '''
        if len(values) != len(self.__values):
            raise ValueError("values must have the same length as the vector.")
        elif not all([isinstance(value, (int, float)) for value in values]):
            raise ValueError("values must be a list of numbers (int or float).")
        else:
            return self.__values.dot(np.array(values))


    def sum_of_values(self):
        '''
        function that returns the sum of the values in the vector.
        :return: int|float
        '''

        return np.sum(self.__values)

    def product_of_values(self):
        '''
        function that returns the product of the values in the vector.
        :return: int|float
        '''

        p = 1
        for i in range(len(self.__values)):
            p *= self.__values[i]

        return p

    def average_of_values(self):
        '''
        function that returns the average of the values in the vector.
        :return: int|float
        '''

        if len(self.__values) == 0:
            raise ValueError("The vector must have at least one value.")
        else:
            return sum(self.__values) / len(self.__values)


    def minimum_of_values(self):
        '''
        function that returns the minimum value of the vector.
        :return: int|float
        '''

        return min(self.__values)

    def maximum_of_values(self):
        '''
        function that returns the maximum value of the vector.
        :return: int|float
        '''
        return max(self.__values)

    def __eq__(self, other):
        '''
        function that checks equality of two vectors.
        :param other:
        :return: bool
        '''
        return self.__name_id == other.__name_id



