import random 
import string

print("Welcome to the password generator")

def main():
    length = int(input("Enter the length of password you want :"))
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolD = string.punctuation
    combine = lowerD + upperD + digitD + symbolD
    x= random.sample(combine,length)
    p = "".join(x)
    print(p)
    main()
    return
main()