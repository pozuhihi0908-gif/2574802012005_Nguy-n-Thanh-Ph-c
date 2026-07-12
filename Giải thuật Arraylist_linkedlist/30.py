class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

capacity = 2
cache = {}

head = Node(0, 0)
tail = Node(0, 0)

head.next = tail
tail.prev = head

def them_dau(node):
    node.next = head.next
    node.prev = head
    head.next.prev = node
    head.next = node

def xoa(node):
    node.prev.next = node.next
    node.next.prev = node.prev

def get(key):
    if key not in cache:
        return -1

    node = cache[key]
    xoa(node)
    them_dau(node)

    return node.value

def put(key, value):
    if key in cache:
        node = cache[key]
        node.value = value
        xoa(node)
        them_dau(node)

    else:
        if len(cache) == capacity:
            xoa_node = tail.prev
            xoa(xoa_node)
            del cache[xoa_node.key]

        node = Node(key, value)
        them_dau(node)
        cache[key] = node

put(1, 10)
put(2, 20)

print(get(1))

put(3, 30)

print(get(2))
print(get(3))