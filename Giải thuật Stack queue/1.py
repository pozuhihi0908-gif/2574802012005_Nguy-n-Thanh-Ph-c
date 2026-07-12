stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

print("Pop:", stack.pop())

print("Top:", stack[-1])

print("Empty:", len(stack) == 0)