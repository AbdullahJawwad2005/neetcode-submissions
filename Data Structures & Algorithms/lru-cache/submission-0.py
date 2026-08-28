class Node:
    def __init__(self, value = None, left = None, right = None, key = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        # intialize capacity and data structures
        self.capacity = capacity
        self.size = 0
        self.lookup = {} # maps the values to addresses of the nodes that already exist
        # the nodes exist in order in the linked list

        # dummy left and right pointers to keep in order and dict connecting them
        self.left = Node()
        self.right = Node()
        self.left.right = self.right
        self.right.left = self.left

    def add(self, node):
        self.size += 1
        temp = self.left.right
        self.left.right = node
        node.left = self.left
        temp.left = node
        node.right = temp

    def remove(self, node):
        # connect the left and right after disconnecting it
        self.size -= 1
        left = node.left
        right = node.right
        left.right = right
        right.left = left

    def get(self, key: int) -> int:
        # return key values if exists
        # otherwise return -1
        if key not in self.lookup:
            return -1

        # exchange position of node to make it the most recent in the list and make it a function as well for reusability
        self.remove(self.lookup[key])
        self.add(self.lookup[key])
        return self.lookup[key].value
    

    def put(self, key: int, value: int) -> None:
        # update the value of key if it exists, makes it recently used
        if key in self.lookup:
            self.lookup[key].value = value
            self.remove(self.lookup[key])
            self.add(self.lookup[key])
        else:
            new_node = Node(value, None, None, key)
            self.lookup[key] = new_node
            self.add(new_node)
            if self.size > self.capacity:
                temp = self.right.left.key
                del self.lookup[temp]
                self.remove(self.right.left)
                

        
