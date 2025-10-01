from abc import abstractmethod, ABC

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):

    def __init__(self, side_a: int, side_b: int):
        self.side_a = side_a
        self.side_b = side_b

    def area(self) -> float:
        return self.side_a * self.side_b

class Square(Shape):

    def __init__(self, side_a: int):
        self.side_a = side_a

    def area(self) -> float:
        return self.side_a ** 2

