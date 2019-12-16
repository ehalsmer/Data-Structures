import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        # toReturn = self.storage.tail.value
        if self.size == 0:
            return
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
