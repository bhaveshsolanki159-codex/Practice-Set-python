def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

while True:
    year = int(input("Enter a year (or type -1 to exit): "))
    if year == -1:
        print("Exiting...")
        break
    if leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
