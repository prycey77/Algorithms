class StackArray():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(-1)
        else:
            print("Stack is empty.")

    def peek(self):
        return self.stack[-1]

    def print_stack(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])
    
x = StackArray()
x.push('one')
x.push('two')
x.push('three')

print(x.peek())

print(x.pop())
print(x.peek())
x.print_stack()