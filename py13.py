inp=int(input())  #get the input
if inp==2:       #check before the given input is 2 or not
    print("yes")
else:
    temp=0
    for i in range(2,inp):   #check the palindomic rule
        if inp%i==0:
            temp=1
            break
    if temp==1:
        print("no")
    else:
        print("yes")

