class CountUp:

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

print(list(CountUp(5)))  # [1, 2, 3, 4, 5]