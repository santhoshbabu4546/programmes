#given number N find the first multiples of 5
inp=int(input())  #get the input
final=[]
for i in range(1,inp+1): #iterate the given range
    final.append(str(i*5))  #calculate the multiples of 5
print(" ".join(final))  #finally join the values
