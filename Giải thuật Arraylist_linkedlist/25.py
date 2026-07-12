class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 2

truoc = Node(0)
truoc.next = head

nhanh = truoc
cham = truoc

for i in range(k + 1):
    nhanh = nhanh.next

while nhanh != None:
    nhanh = nhanh.next
    cham = cham.next

cham.next = cham.next.next

head = truoc.next

tam = head

while tam != None:
    print(tam.data,end=" -> ")
    tam = tam.next

print("None")