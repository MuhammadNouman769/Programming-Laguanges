"""Mini project: manage a small library."""


class Library:
    def __init__(self):
        self.books = []

    def add(self, title):
        self.books.append(title)

    def available(self):
        return sorted(self.books)


def main():
    library = Library()
    for title in input("Books: ").split(","):
        library.add(title.strip())
    print(library.available())


if __name__ == "__main__":
    main()
