"""Practice class state and behavior."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    print(Rectangle(4, 5).area())


if __name__ == "__main__":
    main()
