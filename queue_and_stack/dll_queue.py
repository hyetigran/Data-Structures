import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []

    def enqueue(self, value):
        self.size += 1
        return self.storage.insert(0, value)

    def dequeue(self):
        if self.len() < 1:
            return None
        self.size -= 1
        return self.storage.pop()

    def len(self):
        return self.size
