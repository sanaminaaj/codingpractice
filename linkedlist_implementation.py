class Node:
    def __init__(self):
        self.data=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def insert(self,data):
        current=Node()
        current.data=data
        if self.head==None:
            self.head=current
            self.last=current
        else:
            self.last.next=current
            self.last=current
    def display(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
    def insertFirst(self,data):
        n=Node()
        n.data=data
        n.next=self.head
        self.head=n
        print("after insertion first:")
        self.display()
    def insertLast(self,data):
        n=Node()
        n.data=data
        self.last.next=n
        print("after insertion last:")
        self.display()
    def deleteFirst(self):
        self.head=self.head.next;
        print("deletefirst:")
        self.display()
l1=LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)

l1.insertFirst(100)
l1.insertLast(200)
l1.deleteFirst()
