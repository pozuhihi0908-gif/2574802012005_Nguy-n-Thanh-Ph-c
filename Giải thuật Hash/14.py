size = 10

table = [None] * size

DELETED = "X"

def put(x):

    index = x % size

    while table[index] != None and table[index] != DELETED:
        index = (index + 1) % size

    table[index] = x

def remove(x):

    index = x % size

    while table[index] != None:

        if table[index] == x:
            table[index] = DELETED
            return

        index = (index + 1) % size

put(10)
put(20)
put(30)

print(table)

remove(20)

print(table)