def calculate_coin(coins,notes,amt):

    # a = amt // 5 # Rs. 5 note
    # if amt >= 5:
    #     print("step1")
    #     b = amt - a * 5  # Rs.1 coin
    #     if y >= b:
    #         if x >= a: 
    #            print(f"Rs.1 coins needed: {b}\nRs.5 notes needed: {a}")
    #         else:
    #             print()
    #     else:
    #         print(-1)
    
    req_notes = amt // 5
    

x = int(input("Enter Number of Rs.1 coin you had: "))
y = int(input("Enter Number of Rs.5 Notes you had:"))
amt = int(input("Enter Amount to be made: "))
calculate_coin(x,y,amt)