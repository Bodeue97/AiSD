
from typing import Any

import int as Int


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node = None):
        self.head = node

    def add(self, value:Any):
        node = Node(value)
        node.next = self.head
        self.head = node
    def travel(self):
        cur = self.head
        while cur!=None:
            print(cur.value, end='')
            cur = cur.next
    def node(self, at:Int):
        if self.length()>=at:
            node = self.head
            for x in range(at):
                node = node.next
            return node

    def length(self):
        cur = self.head
        count = 0
        while cur!=None:
            count +=1
            cur = cur.next
        return count



    def append(self, value:Any):
        node = Node(value)
        if self.head ==None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self, value:Any, after:Node):
        if after == None:
            print("Podano wezel spoza listy")
            return
        node = Node(value)
        node.next = after.next
        after.next = node
    def remove(self,after:Node):

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
        for x in range(self.length()-2):
            node = node.next
        node2 = node.next
        node.next = None

        return node2




list_ = LinkedList()
node = Node(3)
assert list_.head == None
list_.add(4)
list_.add(3)
list_.add(2)
list_.add(1)
list_.append(5)
list_.insert(69, list_.node(3))
list_.pop()
print(list_.remove_last().value)
list_.remove(list_.node(999))




list_.travel()







