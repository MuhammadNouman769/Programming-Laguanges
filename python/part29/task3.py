


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self._price = None
        self.price = price          # setter yahan call hoga

    # ---------- @property / @setter ----------
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price negative nahi ho sakti")
        self._price = value

    # ---------- __str__ (user ke liye) ----------
    def __str__(self):
        return f"{self.title} by {self.author} - Rs. {self.price}"

    # ---------- __repr__ (developer ke liye) ----------
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages}, price={self.price})"

    # ---------- __eq__ (title + author same to books equal) ----------
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    # ---------- __lt__ / __gt__ (pages ke hisab se compare) ----------
    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if book in self.books:      # __eq__ use hoga
            print(f"'{book.title}' pehle se maujood hai.")
            return
        self.books.append(book)

    # ---------- __len__ ----------
    def __len__(self):
        return len(self.books)

    # ---------- __getitem__ (index se book, aur loop bhi chalega) ----------
    def __getitem__(self, index):
        return self.books[index]

    def __str__(self):
        return f"{self.name} ({len(self)} books)"


# ================= Use karke dekhein =================
if __name__ == "__main__":
    lib = Library("Muhammad Nouman Library")

    b1 = Book("Uswa-e-Rasool", "Muhammad Nouman", 320, 1200)
    b2 = Book("Meri Aulad Meri Zimma Dari", "Muhammad Nouman", 207, 950)
    b3 = Book("Beti Rehmat-e-Khudawandi", "Muhammad Nouman", 150, 700)
    b4 = Book("Uswa-e-Rasool", "Muhammad Nouman", 320, 1200)  # duplicate

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)
    lib.add_book(b4)                # duplicate message aayega

    print(lib)                      # __str__  -> Muhammad Nouman Library (3 books)
    print(len(lib))                 # __len__  -> 3
    print(lib[0])                   # __getitem__ + __str__
    print(repr(lib[1]))             # __repr__

    print(b1 == b4)                 # __eq__  -> True
    print(b1 > b2)                  # __gt__  -> True (320 > 207)
    print(b3 < b2)                  # __lt__  -> True (150 < 207)

    # __getitem__ ki wajah se for loop bhi chalta hai
    for book in lib:
        print("-", book)

    # sorted() ke liye __lt__ kaafi hai
    for book in sorted(lib.books):
        print(book.title, book.pages)

    # @setter validation
    b2.price = 1000                 # theek
    try:
        b2.price = -50              # error
    except ValueError as e:
        print("Error:", e)