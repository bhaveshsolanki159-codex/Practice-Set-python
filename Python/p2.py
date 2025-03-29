# Write a code to check whether a given number is a palindrome.

def find_palindrome(number):
    num = str(number)
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            return False
    return True


numbers = int(input("Enter the number: "))
print(find_palindrome(numbers))