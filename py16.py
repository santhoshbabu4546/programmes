#dispaly prime numbers between two intervals
inp=list(map(int,input().split()))
final=[]
for p in range(inp[0],inp[1]):
    if p== 2:  # check before the given input is 2 or not
        final.append(str(p))
    else:
        temp = 0
        for i in range(2, p):  # check the palindomic rule
            if p% i == 0:
                temp = 1
                break
        if temp != 1:
            if p!=1:
                final.append(str(p))
print(" ".join(final))
