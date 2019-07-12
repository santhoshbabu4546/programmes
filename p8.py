#camel case 
inp=input().split()  #get teh input
data=list(map(lambda x:x.capitalize(),inp))  #capitalize the first character
print(" ".join(data))    #print thre data
