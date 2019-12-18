import sys
sys.path.append('./dll_queue')
sys.path.append('./dll_stack')
sys.path.append('./doubly_linked_list')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    '''pseudocode:
    if insertion point found:
        create new node
    if value to insert < current node:
        go left
    else:
        go right
    '''
    def insert(self, value):
        parent = None
        current = self
        print('current: ', current)
        while current != None:
            if value < current.value:
                print('in left branch')
                parent = current
                current = current.left
            else:
                print('right branch')
                current = current.right
        print('current after while: ', current)
        current = BinarySearchTree(value)
        parent.left = current
        print('current value should be bst value: ', current.value, 'left: ', current.left, 'right: ', current.right)

    # Return True if the tree contains the value
    # False if it does not
    # searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    # returns the maximum value in the binary search tree.
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # performs a traversal of _every_ node in the tree,
    # executing the passed-in callback function on each tree node value. 
    # There is a myriad of ways to perform tree traversal; in this case any of them should work. 
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

myBST = BinarySearchTree(78)
print(myBST.value, myBST.left)
myBST.insert(12)
print(myBST.value, myBST.right)