#Amstrong number
n=input()                   #get the input
inp=list(map(int,list(n))) #convert into list
sum=0
length=len(inp)            #calcualate length
for value in inp:
    sum=sum+(value**length) #armstrong rule
if sum==int(n):
    print("yes")
else:
    print("no")
