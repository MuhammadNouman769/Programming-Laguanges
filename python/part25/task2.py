from abc import ABC, abstractmethod

class enfource(ABC):
    @abstractmethod
    def enginestart():
        pass


class bike(enfource):
    pass

class Car(enfource):
    pass
