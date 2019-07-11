#given number N find the first multiples of 5
inp=int(input())  #get the input
final=[]
for i in range(1,5): #iterate the given range
    final.append(str(i*inp))  #calculate the multiples of 'N'
print(" ".join(final))  #finally join the values
