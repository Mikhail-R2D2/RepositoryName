# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    class Person:
        """
        Represents a person.

        Attributes:
        - name (str): The name of the person.
        - age (int): The age of the person.
        """

        def init(self, name: str, age: int):
            self.name = name
            self.age = age


    class Calculator:
        """
        Basic calculator class.

        Methods:
        - add (float, float) -> float: Adds two numbers.
        - subtract (float, float) -> float: Subtracts the second number from the first.
        """

        def add(self, num1: float, num2: float) -> float:
            return num1 + num2

        def subtract(self, num1: float, num2: float) -> float:
            return num1 - num2


    class Square:
        """
        Represents a square.

        Attributes:
        - side_length (float): The length of each side of the square.
        """

        def init(self, side_length: float):
            self.side_length = side_length

        def area(self) -> float:
            """
            Calculates the area of the square.

            Returns:
            float: The area of the square.
            """
            return self.side_length ** 2


    pass
