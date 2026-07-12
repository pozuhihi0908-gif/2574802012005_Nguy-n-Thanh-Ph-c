s = "abc"

stack = []

for c in s:
    stack.append(c)

ans = ""

while len(stack) > 0:
    ans += stack.pop()

print(ans)