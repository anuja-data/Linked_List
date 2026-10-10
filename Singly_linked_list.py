# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Linkedlist:
#     def __init__(self):
#         self.head=None

# # Create linked list
#     def append(self,values):
#         for value in values:
#             self.insert_end(value)

#     def insert_end(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head=new_node
#             return

#         temp = self.head
#         while temp.next:
#             temp=temp.next

#         temp.next=new_node

# # 2.Traverse and print

#     def display(self):
#         temp=self.head

#         while temp:
#             print(temp.data,end=" ")
#             temp=temp.next

#         print("None")

# # 3. Insert at specific position

#     def insert_position(self,data,pos):
#         new_node = None(data)

#         if pos < 1:
#             print("Invalid position")
#             return
        
#         if pos == 1:
#             new_node.next =self.head
#             self.head = new_node
#             return
        
#         temp = self.head

#         for i in range(pos-2):
#             if temp is None:
#                 print("Invalid Position")
#                 return 
#             temp=temp.next

#         if temp is None:
#             print("Invalid position")
#             return
        
#         new_node.next = temp.next
#         temp.next = new_node

# # 4. Find middle node
#     def middle(self):
#         slow=self.head
#         fast=self.head

#         if self.head is None:
#             print("List is empty")
#             return

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         print("Middle node:",slow.data)

# # 5.Delete node by value

#     def delete(self,value):
#         temp=self.head

#         if temp and temp.data == value:
#             self.head = temp.next
#             return



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Print node values
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Insert node at position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("List is empty")
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # Delete node at position
    def delete(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Reverse linked list
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    # Sum of consecutive nodes
    def consecutive_sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next


# Main program
list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

print("LinkedList")
list.display()

print("Inserting node at 4th position")
list.insert(Node(100), 4)
list.display()

print("Middle node")
list.middle()

print("Deleting node at 4th position")
list.delete(4)
list.display()

print("Reversed list")
list.reverse()
list.display()

print("Sum of consecutive nodes")
list.consecutive_sum()