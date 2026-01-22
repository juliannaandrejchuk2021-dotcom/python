class Collection:
    def __init__(self,data=None):
        if data is None:
            self._items=[]
        else:
            try:
                self._items=list(data)
            except TypeError:
                self._items=[]

    def add(self,value):
        try:
            self._items.append(value)
        except Exception as e:
            print("Error while adding element: ", e)

    def insert(self,index,value):
        try:
            self._items.insert(index,value)
        except (IndexError,TypeError):
            print("Invalid index for insert")

    def __str__(self):
        return f"Collection {self._items}"
    def remove(self, value):
        try:
            self._items.remove(value)
        except ValueError:
            print("Element not found")

    def pop(self, index=-1):
        try:
            return self._items.pop(index)
        except IndexError:
            print("Index out of range")

c = Collection([1,2,3])
print(c)

c.add(4)
print(c)

c.insert(1, 10)
print(c)

c.remove(2)
print(c)

c.pop()
print(c)

c.pop(100)  
