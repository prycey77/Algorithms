class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node 
            self.length += 1

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.previous = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            new_node.next.previous = new_node
            self.length += 1

    def remove(self, index):
        if self.head == None:
            print("Linked list is empty. Nothing to delete")
            return
        if index == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if index >= self.length:
            index = self.length - 1
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next != None:
            current_node.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return
        
    def print_list(self):
        print(self)
        if self.head == None:
            print('Empty')
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print()


my_linkedlist = DoublyLinkedList()
my_linkedlist.append(10)
my_linkedlist.append(5)
my_linkedlist.append(16)
my_linkedlist.prepend(1)
my_linkedlist.insert(3, 40)
my_linkedlist.print_list()
my_linkedlist.remove(3)
my_linkedlist.print_list()