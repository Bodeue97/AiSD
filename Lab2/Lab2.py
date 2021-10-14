from typing import Any

import int as Int


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def push(self, value: Any):
        node = Node(value)
        node.next = self.head
        self.head = node

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

    def node(self, at: Int):
        if len(self) >= at:
            node = self.head
            for x in range(at):
                node = node.next
            return node

    def __len__(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def append(self, value: Any):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node2 = self.head
            while node2.next != None:
                node2 = node2.next

            node2.next = node

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
                raise ValueError("probujesz usunac node z konca, uzyj remove_last()")
                return
        if after == None:
            raise ValueError("probujesz usunac node spoza listy")
            return
        node = self.head
        while node != after:
            node = node.next
        node = node.next
        after.next = node.next

    def pop(self):
        node = self.head
        self.head = node.next
        return node

    def remove_last(self):
        node = self.head
        for x in range(len(self) - 2):
            node = node.next
        node2 = node.next
        node.next = None
        return node2

class Stack:
    def __init__(self):
       self.head = None

    def __len__(self):
        count = 0
        node = self.head

        while node != None:
            node = node.next
            count+=1

        return count

    def push(self, element:Any):
        node = Node(element)
        if self.head == None:
            self.head = node
        else:
            node2 = self.head
            while node2.next != None:
                node2 = node2.next

            node2.next = node

    def pop(self):
        node = self.head
        for x in range(len(self) - 2):
            node = node.next
        node2 = node.next
        node.next = None
        return node2


    def __str__(self):
        strng = ""
        node = self.head
        tab = []
        while (node != None):
            tab.append(node.value)
            node = node.next
        for x in range((len(tab))):
            strng+="|"+str(tab[-x-1])+"|\n"
        return strng

class Queue:
    def __init__(self):
        self.head = None

    def peek(self):

        return self.head

    def enqueue(self, element:Any):
        node = Node(element)
        if self.head == None:
            self.head = node
        else:
            node2 = self.head
            while node2.next != None:
                node2 = node2.next
            node2.next = node
    def dequeue(self):
        node = self.head
        self.head = node.next
        return node
    def __str__(self):
        node = self.head
        strng = ""
        while node != None:
            strng+=node.value+" "
            node = node.next
        return strng
    def __len__(self):
        count = 0
        node = self.head

        while node != None:
            node = node.next
            count+=1

        return count




# list_ = LinkedList()
# list_.head == None
# list_.push(4)
# list_.push(3)
# list_.push(2)
# list_.push(1)
# list_.append(5)
# list_.insert(666, list_.node(3))
# list_.insert(666, list_.node(332))
# list_.pop()
# print(list_.remove_last().value)
# list_.remove(list_.node(0))
# print(list_)
# print(len(list_))


#
# stack = Stack()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
#
#
# print(stack)
# print(stack.pop().value,"\n")
# print(stack)
# print(len(stack))

#
#
queue = Queue()
queue.enqueue("Andrzej")
queue.enqueue("Bartek")
queue.enqueue("Cecyl")
queue.enqueue("Dariusz")
queue.enqueue("Eugeniusz")
queue.enqueue("Fryderyk")
print(len(queue))
print(queue.peek().value)
queue.dequeue()
print(queue.peek().value)
print(len(queue))
print(queue)