from typing import Any

import int as Int


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def add(self, value: Any):
        node = Node(value)
        node.next = self.head
        self.head = node

    def travel(self):
        node = self.head
        while node != None:
            print(node.value, end='')
            node = node.next

    def node(self, at: Int):
        if self.length() >= at:
            node = self.head
            for x in range(at):
                node = node.next
            return node

    def length(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
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
            print("Podano wezel spoza listy")
            return
        node = Node(value)
        node.next = after.next
        after.next = node

    def remove(self, after: Node):
        if after != None:
            if after.next == None:
                print("probujesz usunac node z konca")
                return
        if after == None:
            print("probujesz usunac node spoza listy")
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
        for x in range(self.length() - 2):
            node = node.next
        node2 = node.next
        node.next = None
        return node2

class Stack:
    def __init__(self):
       self.head = None

    def len(self):
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
        for x in range(self.len() - 2):
            node = node.next
        node2 = node.next
        node.next = None
        return node2


    def print(self):

        node = self.head
        tab = []
        while (node != None):
            tab.append(node.value)
            node = node.next
        for x in range((len(tab))):
            print("|",tab[-x-1],"|\n")
        return

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
    def print(self):
        node = self.head
        while node != None:
            print(node.value, end=' ')
            node = node.next
    def len(self):
        count = 0
        node = self.head

        while node != None:
            node = node.next
            count+=1

        return count



# stack = Stack()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
#
#
# stack.print()
# print(stack.pop().value,"\n")
# print(stack.len())








# list_ = LinkedList()
# node = Node(3)
# list_.head == None
# list_.add(4)
# list_.add(3)
# list_.add(2)
# list_.add(1)
# list_.append(5)
# list_.insert(666, list_.node(3))
# list_.pop()
# print(list_.remove_last().value)
# list_.remove(list_.node(0))
# list_.travel()
queue = Queue()
queue.enqueue("Andrzej")
queue.enqueue("Bartek")
queue.enqueue("Cecyl")
queue.enqueue("Dariusz")
queue.enqueue("Eugeniusz")
queue.enqueue("Fryderyk")
print(queue.len())
print(queue.peek().value)
queue.dequeue()
print(queue.peek().value)
print(queue.len())
queue.print()