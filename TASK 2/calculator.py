flag=1
while flag: #INFINITE LOOP
    #INSTRUCTIONS
    print("*****SELECT AN OPERATION YOU WANT TO PERFORM : *****")
    print('1 : Addition     2 : Subtraction')
    print('3 : Multiplication   4 : Division')
    print('5 : Modulo   6 : Exit')
    inp = int(input("Enter your choice : "))
    
    if inp==6:
        flag=0
        continue
    # TAKING INPUT OF 2 NUMBERS
    # print('Enter two numbers : ')
    # a,b = input().split()
    a,b = input("Enter two numbers (space-seperated) : ").split()

    # CHECKING INPUT IS A NUMBER OR NOT
    if not a.isdigit() or not b.isdigit():
        print("*****Please enter a number as imput.*****")
        continue
    else:
        a,b = float(a), float(b)


    if inp==1:
        print('-------')
        print('Result : ',a+b)
        print('-------')
    elif inp==2:
        print('-------')
        print('Result : ',a-b)
        print('-------')
    elif inp==3:
        print('-------')
        print('Result : ',a*b)
        print('-------')
    elif inp==4:
        print('-------')
        print('Result : ',a/b)
        print('-------')
    elif inp==5:
        print('-------')
        print('Result : ',a%b)
        print('-------')
    else:
        print("*****Invalid Input, Do you want to exit? (y/n)*****")
        s = str(input())
        if s=='y' or s=='Y':
            flag=0
        else:
            continue
        