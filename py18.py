#Amstrong number in the given interval
inp=list(map(int,input().split()))
final=[]
for i in range(inp[0]+1,inp[1]):
    sum = 0
    nex=list(map(int,list(str(i))))  #integer is not iteratable
    length = len(nex)  # calcualate length
    for value in nex:
        sum = sum + (value ** length)  # armstrong rule
    if sum == i:
        final.append(str(sum))
print(" ".join(final))
