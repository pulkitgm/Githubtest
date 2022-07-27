print("Converting celsius to fahrenheit  \n")
S= int(input("Enter temprature starting Range:- ")) #start temp value
E= int(input("Enter Temprature Ending poing:- ")) #end temp value
W= int(input("Enter Step count:- ")) #setup size value


while S <= E:
    C = (S*1.8)+32
    print(S, int(C))
    S = S+W
