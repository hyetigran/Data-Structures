import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []
    
    def __str__(self):
        return f"{self.storage}"

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        if self.len() < 1:
            return None
        self.size -= 1
        return self.storage.pop()

    def len(self):
        return self.size
d = Stack()

d.push(1)
d.push(2)
d.push(3)
print(d)