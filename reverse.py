class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Insert
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        p = 1
        temp = self.head

        while p != pos - 1:
            temp = temp.next
            p += 1

        new_node.next = temp.next
        temp.next = new_node

    # Delete
    def delete(self, pos):
        if self.head == None:
            print("Linked List is empty")
            return

        if pos == 1:
            self.head = self.head.next
            return

        p = 1
        temp = self.head

        while p != pos - 1:
            if temp.next == None:
                print("Invalid position")
                return

            temp = temp.next
            p += 1

        if temp.next == None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Reverse
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Display
    def display(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

# Create Linked List
list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(48))
list.append(Node(55))

print("Original Linked List:")
list.display()

print("After inserting 100 at position 4:")
list.insert(Node(100), 4)
list.display()

print("After deleting position 4:")
list.delete(4)
list.display()

print("Reversed Linked List:")
list.reverse()
list.display()


# WAP to print sum of 2 consecutive nodes in sll.