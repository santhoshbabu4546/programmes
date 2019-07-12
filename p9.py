
#count the number of prime numbers for the specified given interval(inclusive)
inp=list(map(int,input().split()))  #get the input
count=0                             
for p in range(inp[0],inp[1]+1):    #range
    c=0
    if p!=1:                        # 1 is nether the prime nor the nor the composite
        if p==2:
            count=count+1
        else:
            for i in range(2,p):
                if p%i==0:               #check the prime not
                    c=1
                    break
            if c==0:
                count=count+1              #incerement the count
print(count)                      #print the count

