class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(3)

tam = head

while tam.data != 1:
    tam = tam.next

node = Node(2)

node.next = tam.next
tam.next = node

tam = head

while tam != None:
    print(tam.data, end=" -> ")
    tam = tam.next

print("None")