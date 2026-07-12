class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

size = 5
table = [None] * size

def put(key, value):
    index = ord(key) % size

    tam = table[index]

    while tam != None:
        if tam.key == key:
            tam.value = value
            return
        tam = tam.next

    node = Node(key, value)
    node.next = table[index]
    table[index] = node

def get(key):
    index = ord(key) % size

    tam = table[index]

    while tam != None:
        if tam.key == key:
            return tam.value
        tam = tam.next

    return -1

def remove(key):
    index = ord(key) % size

    tam = table[index]
    truoc = None

    while tam != None:
        if tam.key == key:
            if truoc == None:
                table[index] = tam.next
            else:
                truoc.next = tam.next
            return

        truoc = tam
        tam = tam.next

put("a",1)
put("b",2)
put("f",3)

print(get("a"))

remove("a")

print(get("a"))