"""Mini project: manage a small library."""


class Library:
    def __init__(self):
        self.books = []

    def add(self, title):
        self.books.append(title)

    def available(self):
        available_books = self.books[:]
        index = 1
        book_count = 0
        for _book in available_books:
            book_count += 1
        while index < book_count:
            current = available_books[index]
            previous = index - 1
            while previous >= 0 and available_books[previous] > current:
                available_books[previous + 1] = available_books[previous]
                previous -= 1
            available_books[previous + 1] = current
            index += 1
        return available_books


def main():
    library = Library()
    for title in input("Books: ").split(","):
        library.add(title.strip())
    print(library.available())


if __name__ == "__main__":
    main()
