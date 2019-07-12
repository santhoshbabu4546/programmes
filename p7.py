#given string s swap the string in evn position and odd position
inp=list(input())  #get teh input
odd=[]
even=[]
data=[]
for i in range(len(inp)):
    if i%2==0:
        even.append(inp[i])  #appendd the even position
    else:
        odd.append(inp[i])  #append the even position
final=list(map(lambda x,y:x+y,odd,even))  #swap the values
print("".join(final))  #print teh final values
         

