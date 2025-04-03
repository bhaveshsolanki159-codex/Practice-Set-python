def max_num(num1,num2):
    if num1 >= num2:
        return -1
    
    create_list = []
    for i in range(num1,num2+1):
        if 10 <= i <= 99:
            num = sum(int(digit) for digit in str(i))
            if num % 3 == 0 and i % 5 == 0:
                create_list.append(i)

    return max(create_list) if create_list else -1



print(max_num(10, 30))
print(max_num(50, 60))
print(max_num(1, 9))    
print(max_num(100, 110))






          