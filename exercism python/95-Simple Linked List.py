class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message

class Node:
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def value(self):
        return self.data

    def next(self):
        return self.next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:

    def __init__(self, values=None):
        self._head = None
        
        if values != None:
            for value in values:
                self.push(value)
            
    def __iter__(self):
        result = []
        current = self._head

        while current:
            yield current.data
            current = current.next_node
    
    def __len__(self):
        current = self._head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self._head
        self._head = new_node

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        pop_value = self._head.data
        self._head = self._head.next_node
        return pop_value

    def reversed(self):
        previous = None
        current = self._head

        while current:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node

        self._head = previous

        current = self._head
        while current:
            yield current.data
            current = current.next_node
        