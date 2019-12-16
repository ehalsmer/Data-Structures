import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        print("Value we're pushing:", value)
        self.storage.add_to_head(value)
        # print("STORAGE", self.storage)

    def pop(self):
        # toReturn = self.storage.tail.value
        print('In POP ')
        if self.size == 0:
            print("self.size is 0")
            return
        else :
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
