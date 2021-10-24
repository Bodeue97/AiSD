from typing import Any




class Node:
    def __init__(self, value:Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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
        for x in range(len(self)):
            if node.next != None:
                strng+=str(node.value)+" -> "
            if node.next == None:
                strng+=str(node.value)
            node = node.next
        return strng

    def push(self, value: Any):
        if self.head == None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def append(self, value: Any):
        if self.head != None:
            node = self.tail
            node.next = Node(value)
            self.tail = node.next
        else:
            self.push(value)

    def node(self, at: int):
        if len(self) == 0:
            raise ValueError("lista jest pusta")
        if at < 0:
            raise ValueError("Podano indeks < 0 ")
        if at > len(self)-1:
            raise ValueError("Podano indeks spoza listy")
        if at == len(self)-1:
            node = self.tail
        if len(self) > at:
            node = self.head
            for x in range(at):
                node = node.next
        return node

    def insert(self, value: Any, after: Node):

        if after == self.tail:
            self.append(value)
            return
        if after == None:
            raise ValueError("Podany wezel nie istnieje")
            return
        node = Node(value)
        node.next = after.next
        after.next = node

    def pop(self):
        if self.head != None:
            node = self.head
            self.head = node.next
            return node
        else:
            raise ValueError("lista jest pusta")

    def remove_last(self):
        node = self.head
        if self.head == None:
            raise ValueError("lista jest pusta")
        if len(self) == 1:
            deleted = self.head
            self.head = None
            return deleted
        else:
            while node.next != self.tail:
                node = node.next
        self.tail = node
        deleted = node.next
        node.next = None


        return deleted

    def remove(self, after: Node):
        node = self.head
        if len(self) == 1:
           raise ValueError("lista ma tylko 1 element")
        if after.next == self.tail:
            deleted = self.tail
            self.remove_last()
        else:
            while node.next != after:
                node=node.next
            deleted = node.next
            node.next = after.next

        return deleted

class Stack:
    def __init__(self):
       self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        strng = ""

        for x in range(len(self._storage)):
            strng+="|"+ str(self._storage.node(x).value)+"|\n"

        return strng
    def push(self, element:Any):
        self._storage.push(element)


    def pop(self):
        if len(self._storage) != 0:
            return self._storage.pop().value
        else:
            raise ValueError("Stos jest pusty")

class Queue:
    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        strng = ""

        for x in range(len(self._storage)):
            strng += str(self._storage.node(x).value)+" "

        return strng

    def peek(self):
        if len(self._storage) != 0:
            return self._storage.tail.value
        else:
            raise ValueError("Kolejka jest pusta")

    def enqueue(self, element:Any):
        self._storage.push(element)

    def dequeue(self):
        if len(self._storage) != 0:
            return self._storage.remove_last().value
        else:
            raise ValueError("Kolejka jest pusta")










