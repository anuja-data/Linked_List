class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Concatenate two linked lists
    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = list2.head


# Main program
list1 = LinkedList()
list2 = LinkedList()

list1.append(10)
list1.append(20)
list1.append(30)

list2.append(40)
list2.append(50)
list2.append(60)

print("First Linked List")
list1.display()

print("Second Linked List")
list2.display()

list1.concatenate(list2)

print("Concatenated Linked List")
list1.display()