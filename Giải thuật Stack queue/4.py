size = 3

stack = []

if len(stack) == 0:
    print("Underflow")

stack.append(1)
stack.append(2)
stack.append(3)

if len(stack) == size:
    print("Overflow")