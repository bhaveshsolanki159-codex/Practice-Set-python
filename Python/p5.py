def final_fee(degree,marks,course_fee):
    scholarship = 0
    if degree == 'arts':
        if marks >= 90:
            scholarship = 50
            return scholarship
        elif marks % 2 != 0:
            scholarship = 5
            return scholarship
    elif degree == 'engineering':
        if marks >= 85:
            scholarship = 50
            return scholarship
        elif marks % 7 == 0:
            scholarship = 5
            return scholarship
    else:
        return "Invalid degree"
    
    scholarship_amt = (course_fee * scholarship) / 100
    return scholarship_amt

num_students = 500

for i in range(1, num_students + 1):
    print(f"\nStudent {i}:")

    degree = input("Enter course: (arts/engineering)").lower()
    marks = int(input("Enter marks: "))
    course_fee = int(input("Enter course fee: "))

    scholarship_amt = final_fee(degree,marks,course_fee)

    if isinstance(scholarship_amt, str):
        print("Invalid degree")
    else:
        fee = course_fee - scholarship_amt
        print(f"Scholarship amount: {scholarship_amt}")
        print(f"Total fee to be paid: {fee}")