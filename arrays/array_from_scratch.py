class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self._shift_items(index)

    def _shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


new_array = MyArray()
new_array.push('Hello1')
new_array.push('Hello2')
new_array.push('Hello3')
new_array.push('Hello4')
print(new_array.get(0))
print(new_array.get(3))
print(new_array.pop())
print(new_array.data)
new_array.delete(0)
print(new_array.data)
new_array.delete(1)
print(new_array)