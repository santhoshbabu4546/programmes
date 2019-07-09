#given 2 numbers N,K and an array   of N integers ,find the sum of the first k integers
inp=list(map(int,input().split()))    #get the N,K values
values=list(map(int,input().split())) #get the N number of vallues
print(sum(values[:inp[1]])) #print the sum of the first k integers
