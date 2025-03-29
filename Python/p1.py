# Write a code to find the minimum among three given numbers.


def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num :
            min_num = num
    return min_num

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: "))for i in range(n)]

print("The minimum number is: ", find_minimum(numbers))

#print(min(numbers))