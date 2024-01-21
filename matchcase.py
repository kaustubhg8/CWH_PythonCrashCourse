# New addition from Python 3.10 onwards

a = int(input("Enter number: "))
match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 22:
        print("Case is 22")
    case 13:
        print("Case is 13")
    case _:
        print("No match found")


#  Quiz : Write a program to print table between 1 -10

table = int(input("Which table you want: "))

match table:
    case 1:
        print(list(range(0,100,table))[1:11])
    case 2:
        print(list(range(0,100,table))[1:11])
    case 3:
        print(list(range(0,100,table))[1:11])
    case 4:
        print(list(range(0,100,table))[1:11])
    case 5:
        print(list(range(0,100,table))[1:11])
    case 6:
        print(list(range(0,100,table))[1:11])
    case 7:
        print(list(range(0,100,table))[1:11])
    case 8:
        print(list(range(0,100,table))[1:11])
    case 9:
        print(list(range(0,100,table))[1:11])
    case 10:
        print(list(range(0,101,table))[1:11])
    case _:
        print("Please enter value between 1 to 10")