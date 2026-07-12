class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head.next.next.next = head.next

cham = head
nhanh = head

co = False

while nhanh != None and nhanh.next != None:
    cham = cham.next
    nhanh = nhanh.next.next

    if cham == nhanh:
        co = True
        break

if co:
    print("Có chu trình")
else:
    print("Không có chu trình")