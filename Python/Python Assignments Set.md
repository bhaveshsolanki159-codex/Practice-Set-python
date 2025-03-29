**Fundamentals of Python**  
**Day \-1**

1. Write a code to find the minimum among three given numbers.  
2. Write a code to check whether a given number is a palindrome.  
3. Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to the sum if it is divisible by 4\. It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.  
4. A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself.Write a program to check whether a number is armstrong or not.   
     
5. JIT University offering degree courses to students has decided to provide scholarship based on the following details:

| Branch of study | Score (%) | Scholarship % | Remarks |
| ----- | ----- | ----- | ----- |
| Arts | Score is at least 90 | 50 | The student is eligible only for one scholarship% even if both the score conditions are valid for the given branch of study. In such cases, students are eligible for the highest scholarship% applicable among the two. |
| Arts | Score is an odd number | 5 |  |
| Engineering | Score is more than 85 | 50 |  |
| Engineering | Score is divisible by 7 | 5 |  |

   If there are 500 students who have joined the university, write a code to calculate and display the final fees to be paid by each student.

   You may accept the branch of study, score and course fee as inputs for each student and calculate the final fees to be paid by each student based on formulae given below:

   Scholarship amount=course fee \* (scholarship%)

   Final fee= course fee \- scholarship amount

6. The flight ticket rates for a round-trip (Mumbai-\>Dubai) were as follows:  
* Rate per Adult: Rs. 37550.0  
* Rate per Child: 1/3rd of the rate per adult  
* Service Tax: 7% of the ticket amount (including all passengers)  
* As it was a holiday season, the airline also offered a 10% discount on the final ticket cost (after inclusion of the service tax).  
* Find and display the total ticket cost for a group which had adults and children.

**Day-2** 

    7\.  Write a python program that displays a message as follows for a given number:

* If it is a multiple of three, display "Zip"  
* If it is a multiple of five, display "Zap".  
* If it is a multiple of both three and five, display "Zoom".  
* If it does not satisfy any of the above given conditions, display "Invalid".

    8\.	A teacher in a school wants to find and display the grade of a student based on his/her percentage score. The criterion for grades is as given below:

| Score (both inclusive) | Grade |
| :---- | :---- |
| Between 80 and 100 | A |
| Between 73 and 79 | B |
| Between 65 and 72 | C |
| Between 0 and 64 | D |
| Any other value | Z |

Assume that the percentage score is a whole number. Write a python program for the above requirement.

9\. Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

It should display the product of the three values except when one of the integer value is 7\. In that case, 7 should not be included in the product and the values to its left also should not be included.  
If there is only one value to be considered, display that value itself. If no values can be included in the product, display \-1.

Note: Assume that if 7 is one of the positive integer values, then it will occur only once. Refer the sample I/O given below.

| Sample Input | Expected Output |
| ----- | ----- |
| 1, 5, 3 | 15 |
| 3, 7, 8 | 8 |
| 7, 4, 3 | 12 |
| 1, 5, 7 | \-1  |

10\. You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display \-1.

| Sample Input |  |  | Expected Output |  |
| ----- | :---- | :---- | ----- | :---- |
| Available Rs. 1 coins | Available Rs. 5 notes | Amount to be made | Rs. 1 coins needed | Rs. 5 notes needed |
| 2 | 4 | 21 | 1 | 4 |
| 11 | 2 | 11 | 1 | 2 |
| 3 | 3 | 19 | \-1  |  |

**Day \-3**

11\. Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.

12\. ARS Gems Store sells different varieties of gems to its customers.

Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased. Any purchase with a total bill amount above Rs.30000 is entitled to 5% discount. If any gem required by the customer is not available in the store, then consider total bill amount to be \-1.

Assume that quantity required by the customer for any gem will always be greater than 0\.

Perform case-sensitive comparison wherever applicable.

gems\_list=\["Emerald","Ivory","Jasper","Ruby","Garnet"\]

\#Price of gems available in the store. gems\_list and price\_list have one-to-one correspondence  
price\_list=\[1760,2119,1599,3920,3999\]

\#List of gems required by the customer  
reqd\_gems=\["Ivory","Emerald","Garnet"\]

\#Quantity of gems required by the customer. reqd\_gems and reqd\_quantity have one-to-one correspondence  
reqd\_quantity=\[3,10,12\]

13\. Write a python function to check whether three given numbers can form the sides of a triangle.  
Hint  
: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.

14\. Write a python program to solve a classic ancient Chinese puzzle.  
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

| Sample Input | Expected Output |
| ----- | ----- |
| heads-150 legs-400 | 100 50 |
| heads-3 legs-11 | No solution |
| heads-3 legs-12 | 0 3 |
| heads-5 legs-10 | 5 0 |

15\. Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

1. Always num1 should be less than num2  
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied  
   1. Sum of the digits of the number is a multiple of 3  
   2. Number has only two digits  
   3. Number is a multiple of 5  
3. Display the maximum element from the list

In case of any invalid data or if the list is empty, display \-1.

16\. Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:  
The ticket number should be generated as airline:src:dest:number  
where

1. Consider AI as the value for airline  
2. src and dest should be the first three characters of the source and destination cities.  
3. number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.  
Note: If passenger count is less than 5, return the list of all generated ticket numbers.

| Sample Input | Expected Output |
| ----- | ----- |
| airline \= AI source \= Bangalore destination \= London no\_of\_passengers \= 10 | \['AI:Ban:Lon:106', 'AI:Ban:Lon:107', 'AI:Ban:Lon:108', 'AI:Ban:Lon:109', 'AI:Ban:Lon:110'\] |
| airline \= BA source \= Australia destination \= France no\_of\_passengers \= 2 | \['BA:Aus:Fra:101', 'BA:Aus:Fra:102'\]  |

17\. Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary

{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 

and use it to translate your Christmas wishes from English into Swedish.

That is, write a python function translate() that accepts the bilingual dictionary and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words.

**Day-4**

18\. The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.

Assume that the following information are given:  
Price per litre of fuel \= 70  
Mileage of the bus in km/litre of fuel \= 10  
Price(Rs) per ticket \= 80

The bus runs on multiple routes having different distance in kms and number of passengers.  
Write a function to calculate and return the profit earned (Rs) in each route. Return \-1 in case of loss.

19\. Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program.

| Sample Input | Expected Output |
| :---- | ----- |
| AAAABBBBCCCCCCCC | 4A4B8C |
| AABCCA | 2A1B2C1A  |

20\. Write a function, check\_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return false.

Note: Initialize the string with various values and test your program. Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW etc. 

21\. Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:  
{  
"P":"Pediatrics",  
"O":"Orthopedics",  
"E":"ENT  
}

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.

Note:

1. Assume that there is always only one medical speciality which is visited by maximum number of patients.  
2. Perform case sensitive string comparison wherever necessary.

| Sample Input | Expected Output |
| ----- | ----- |
| \[101,P,102,O,302,P,305,P\] | Pediatrics |
| \[101,O,102,O,302,P,305,E,401,O,656,O\] | Orthopedics |
| \[101,O,102,E,302,P,305,P,401,E,656,O,987,E\] | ENT  |

