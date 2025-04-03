def ticket_num(airline,src,dest,passenger):
    tickets = []
    for j in range(101, 101+passenger):
        ticket = f"{airline}:{src[:3]}:{dest[:3]}:{j}"
        tickets.append(ticket)
    return tickets

print(ticket_num('AI','Bangalore','London',10))

