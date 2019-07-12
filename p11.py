#check the given day is holiday or not
inp=input()
if inp in ["Saturday","Sunday"]:   #holiday
    print("yes")
elif inp in ["Monday","Tuesday","Wednesday","Thursday","Friday"]:  #not a holiday
    print("no")
