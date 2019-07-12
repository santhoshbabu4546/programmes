#rotate the array
inp=list(map(int,input().split()))  #get the input size and number of times rotate
values=input().split()
values="".join(values)    #convert into string
if len(values)==1:
    print(values)
else:
    for _ in range(inp[1]):
        values=(str(values[-1])+str(values[:len(values)-1]))   #rotation
    print(" ".join(values))       #print the values
