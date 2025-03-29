def check_num(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Zoom")
    elif num % 3 == 0:
        print("Zip")
    elif num % 5 == 0:
        print("Zap")
    else:
        print("Invalid")

number = int(input("Enter a number: "))
check_num(number)
