
#given teo string check whether the given sring is differ only once
inp=input().split()
count=0
if len(inp[0])==len(inp[1]):     #two string length must equval
    for i in range(len(inp[0])):

        if inp[0][i]!=inp[1][i]:    #check the given character 
            count=count+1
            if count>1:             #break the differ is more then 2
                break
    if count==1:
        print("yes")
    else:
        print("no")
else:
    print("no")


