#dispaly even numbers between two intervals
inp=list(map(int,input().split()))  #get the input
final=[]                            #append the final
for i in range(inp[0]+1,inp[1]):    #iteration
    if i%2==0:
        final.append(str(i))        #append the even value to the final
print(" ".join(final))              #print the final

