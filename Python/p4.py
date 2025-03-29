def find_armstrong(number):
    num = str(number)
    if len(num) >= 2:
        sum = 0
        for i in num:
            sum += int(i) ** len(num)
        print(sum)
        return sum == number
    else:
        return False

num = int(input("Enter number: "))
print(find_armstrong(num))