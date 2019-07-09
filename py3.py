#check the given charactor is vowel or consonants
inp=input()
letter=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v''w','x','y','z']  #make consonat values in oone list
vowel=['a','e','i','o','u']  #vowel in one list
inp=inp.casefold()  #make the casefold to make
if inp in vowel:
    print("Vowel") #if it is vowel print vowel
elif inp in letter:
    print("Consonant") #else print consonant
else:
    print("invalid")  #not statified print invalid


