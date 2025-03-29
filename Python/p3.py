# Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to the sum if it is divisible by 4. It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.


def find_sumby4(number):
    if number % 4 == 0:
        sum = number
        choice = input("Want to add more numbers? (yes/no): ")
        if choice.lower() == "yes":
            num = int(input("Enter a number: "))
            sum = sum + num
            return find_sumby4(sum)
        else:
            return sum
    else:
        return "Number is not divisible by 4"

num = int(input("Enter a number: "))
print(find_sumby4(num))
    