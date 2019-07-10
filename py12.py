#check whether the given number is palindrome or not

inp=input()
if inp==inp[::-1]:   #inp[::-1] reverse the string and check
    print("yes")
else:
    print("no")
