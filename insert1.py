class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node

    def insert(self, new_node, pos):
        # Insert at beginning
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        # Move to the node before the required position
        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        # Position is invalid
        if temp is None:
            print("Invalid position")
            return

        # Insert the node
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    def total(self):
        total = 0
        temp = self.head

        while temp:
            total += temp.data
            temp = temp.next

        print("Sum =", total)


list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))

list.display()
list.total()

# Insert 100 at position 3
list.insert(Node(100), 3)

list.display()
list.total()
