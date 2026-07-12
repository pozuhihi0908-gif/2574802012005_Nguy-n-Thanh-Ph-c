h = [2,1,5,6,2,3]

stack = []

maxArea = 0

i = 0

while i < len(h):

    if len(stack)==0 or h[stack[-1]] <= h[i]:

        stack.append(i)

        i += 1

    else:

        top = stack.pop()

        if len(stack)==0:
            area = h[top] * i
        else:
            area = h[top] * (i-stack[-1]-1)

        if area > maxArea:
            maxArea = area

while len(stack)>0:

    top = stack.pop()

    if len(stack)==0:
        area = h[top] * i
    else:
        area = h[top] * (i-stack[-1]-1)

    if area > maxArea:
        maxArea = area

print(maxArea)