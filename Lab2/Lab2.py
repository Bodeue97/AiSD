from typing import Any




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    def push(self, value: Any):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.tail = node.next

    def __len__(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def __str__(self):
        strng = ""
        node = self.head
        while node != None:
            if node.next != None:
                strng+=str(node.value)+"->"
            else:
                strng+=str(node.value)
            node = node.next
        return strng

    def node(self, at: int):
        if at < 0:
            raise ValueError("podano indeks < 0")

        if len(self) > at:
            node = self.head
            for x in range(at):
                node = node.next
        else:
            raise ValueError("Podano indeks spoza listy")
        return node

    def append(self, value: Any):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node


    def insert(self, value: Any, after: Node):


        if after == None:
            raise ValueError("Podano wezel spoza listy")
            return
        node = Node(value)
        node.next = after.next
        after.next = node

    def remove(self, after: Node):
        if after != None:
            if after.next == None:
                raise ValueError("probujesz usunac node spoza listy")
                return
        if after == None:
            raise ValueError("probujesz usunac node spoza listy")
            return
        node = self.head
        while node != after:
            node = node.next
        node = node.next
        node2 = node
        after.next = node.next
        return node2

    def pop(self):
        node = self.head
        self.head = node.next
        return node

    def remove_last(self):
        node = self.tail.next
        self.tail.next = None

        return node

class Stack:
    def __init__(self):
       self._storage = None

    def __len__(self):
        count = 0
        node = self._storage

        while node != None:
            node = node.next
            count+=1

        return count

    def push(self, element:Any):
        node = Node(element)
        if self._storage == None:
            self._storage = node
        else:
            node2 = self._storage
            while node2.next != None:
                node2 = node2.next

            node2.next = node

    def pop(self):
        node = self._storage
        for x in range(len(self) - 2):
            node = node.next
        node2 = node.next
        node.next = None
        return node2


    def __str__(self):
        strng = ""
        node = self._storage
        tab = []
        while (node != None):
            tab.append(node.value)
            node = node.next
        for x in range((len(tab))):
            strng+="|"+str(tab[-x-1])+"|\n"
        return strng

class Queue:
    def __init__(self):
        self._storage = None

    def peek(self):

        return self._storage

    def enqueue(self, element:Any):
        node = Node(element)
        if self._storage == None:
            self._storage = node
        else:
            node2 = self._storage
            while node2.next != None:
                node2 = node2.next
            node2.next = node
    def dequeue(self):
        node = self._storage
        self._storage = node.next
        return node
    def __str__(self):
        node = self._storage
        strng = ""
        while node != None:
            strng+=node.value+" "
            node = node.next
        return strng
    def __len__(self):
        count = 0
        node = self._storage

        while node != None:
            node = node.next
            count+=1

        return count




lista = LinkedList()
lista.push(3)
lista.push(5)
lista.append(10)
lista.insert(60, lista.node(0))
print(lista.remove(lista.node(1)).value)



print(lista)
