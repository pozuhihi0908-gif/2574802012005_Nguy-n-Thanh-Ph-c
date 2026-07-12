s="([]{})"

stack=[]

ok=True

for c in s:

    if c=="(" or c=="[" or c=="{":

        stack.append(c)

    else:

        if len(stack)==0:

            ok=False
            break

        x=stack.pop()

        if c==")" and x!="(":
            ok=False

        if c=="]" and x!="[":
            ok=False

        if c=="}" and x!="{":
            ok=False

if len(stack)!=0:
    ok=False

print(ok)