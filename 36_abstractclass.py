from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea():
        return 0
class Rectangle(Shape):
    def printarea():
        return 0
obj = Rectangle()