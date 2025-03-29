def calculate_ticket_fare(num_adult, num_children):

    # Ticket rates
    adult_rate = 37550.0
    children_rate = 37550.0/3

    # calculating total fare icluding service tax
    fare_of_ticket = (num_adult*adult_rate)+(num_children*children_rate)
    total_fare = fare_of_ticket + (0.07 * fare_of_ticket) #service tax = 7%

    # final fare with discount
    final_fare = total_fare - (total_fare*0.1) #10% discount

    return final_fare

num_adult = int(input("Enter the number of adults: "))
num_children = int(input("Enter the number of children: "))

total_cost = calculate_ticket_fare(num_adult, num_children)
print(f"Total cost of the ticket is:\n Rs .{total_cost:.2f}")



    

