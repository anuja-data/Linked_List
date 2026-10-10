class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node #appending new node
    def insert(self,new_node,pos):
        if pos==1:
            new_node.next=self.head
            self.head=new_node
        else:
            p=1
            while (p!=pos-1):
                temp=temp.next
                p+=1
                print(p)
            new_node.next
    def print(self,new_node,pos):
        temp=self.head
        while temp:
            # if temp.data >0:
            sum+=temp.data  
            # COUNT+=1
            temp=temp.next
        print(sum)

list=linkedlist()
n1=Node(10)
# n2=Node(-20) 
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))

list.insert(Node(100),3)
# list.append(Node(-40))

list.print()