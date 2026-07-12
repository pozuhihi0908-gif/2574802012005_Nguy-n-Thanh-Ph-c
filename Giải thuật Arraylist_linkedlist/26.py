class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.prev = head

node2.next = node3
node3.prev = node2

tam = head

while tam != None:
    print(tam.data, end=" -> ")
    cuoi = tam
    tam = tam.next

print("None")

while cuoi != None:
    print(cuoi.data, end=" -> ")
    cuoi = cuoi.prev

print("None")