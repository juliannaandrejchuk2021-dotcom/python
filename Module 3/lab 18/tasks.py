class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

class Iterable:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return Iterator(self.data)
    def append(self, value):
        self.data.append(value)
    def __getitem__(self,item):
        assert isinstance(item,int)
        assert item>=0
        return self.data[item]

def FactorialGenerator(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

def FibonacciGenerator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b