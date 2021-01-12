class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    

    def push(self, data):
        new_item = Node(data)
        if self.top == None:
            self.top = new_item
            self.bottom = new_item
        else:
            new_item.next = self.top
            self.top = new_item
        self.length += 1
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def pop(self):
        if self.top == None:
            print('Stack empty')
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None

    def print_stack(self):
        if self.top is None:
            print('Stack is empty.')
        else:
            current_pointer = self.top
            while current_pointer != None:
                print(current_pointer.data)
                current_pointer = current_pointer.next


my_stack = Stack()

my_stack.push("one")
my_stack.push("two")
my_stack.push("three")
print(my_stack.bottom.data)
print(my_stack.top.data)
print(my_stack.peek())
my_stack.pop()
my_stack.push("Banana!")
print(my_stack.peek())
my_stack.print_stack()