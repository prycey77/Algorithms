class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
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
            self.head = new_node 
            self.length += 1

    def insert(self, index, data):
        if index >= self.length:
            if index > self.length:
                print("That position is unavailable")
            new_node = Node(data)
            self.tail.next = new_node
            self.length += 1
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1


    def print_list(self):
        if self.head == None:
            print('Empty')
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print()


my_linkedlist = LinkedList()
my_linkedlist.append(10)
my_linkedlist.append(5)
my_linkedlist.append(16)
my_linkedlist.prepend(1)
my_linkedlist.insert(3, 40)
my_linkedlist.print_list()