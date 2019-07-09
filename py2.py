#check the given number is even or odd
input_v=input()     #get the input value
if input_v.isdigit() and int(input_v)>0:  #check the given input is digit and greater then 0
    if int(input_v)%2==0: #chek the given number is divisible by 2 or not.
        print("Even")
    else:
        print("Odd")  #print if it is not divisible by 2
else:
    print("invalid")  #if it is special charator print invalid
