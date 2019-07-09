inp=input()  #get the input
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t','u','v''w','x','y','z'] #make the letter list
inp=inp.casefold()# to make case insensitive
if inp in letter:
    print("Alphabet")  #if it is alphate print it
else:
    print("No") #else print No
