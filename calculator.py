#insert any value in between 1 to 5, if insert 6 then progam will exit, if insert any other number then you will get invalid Operation output


while True:
    choice = int(input())
    if (choice>=1 and choice<=5):
        num1 = int(input())
        num2 = int(input())
        if choice == 1: 
            res = num1 + num2
            print(res)
        elif choice == 2: 
            res = num1 - num2
            print(res)
        elif choice == 3: 
            res = num1 * num2
            print(res)
        elif choice == 4: 
            res = num1 // num2
            print(res)
        elif choice == 5:
            res = num1 % num2
            print(res)
    elif choice == 6:
        exit()
    else:
        print("Invalid Operation")
