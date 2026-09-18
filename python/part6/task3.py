"""Practice multiple inheritance."""


class Printable:
    def label(self):
        return "printable"


class Storable:
    def save(self):
        return "saved"


class Document(Printable, Storable):
    pass


def main():
    document = Document()
    print(document.label(), document.save())


if __name__ == "__main__":
    main()
