class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

node1 = Node(2)
head = node1

node2 = Node(5)
node1.next = node2

tam = head

while tam != None:
    print(tam.data, end=" -> ")
    tam = tam.next

print("None")