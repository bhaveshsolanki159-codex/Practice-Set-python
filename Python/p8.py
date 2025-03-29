def studend_score(marks):
    if marks >= 80:
        return "A"
    elif marks >= 73 and marks < 80:
        return "B"
    elif marks >= 65 and marks < 73:
        return "C"
    elif marks >= 0 and marks < 65:
        return "D"
    else:
        return "Z"
i=0
while(True):
    marks = int(input("Enter marks of student " + str(i+1) + ": "))
    print("Your grade is: ", studend_score(marks))
    i=i+1
    
