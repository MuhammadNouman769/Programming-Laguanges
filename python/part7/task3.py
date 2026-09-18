"""Practice association between objects."""


class Engine:
    def start(self):
        return "engine started"


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()


def main():
    print(Car(Engine()).start())


if __name__ == "__main__":
    main()
