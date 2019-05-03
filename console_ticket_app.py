TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("{} tickets left.".format(tickets_remaining))
    name = input("Hey there! What is your name?  ")
    num_tickets = input("Nice to meet you, {}. How many tickets would you like?  ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("Sorry. There are only {} tickets left.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no. {}. Please try again.".format(err))
    else:
        total_cost = calculate_price(num_tickets)
        print("Awesome! That'll be ${}.".format(total_cost))
        confirm = input("Would you like to continue? Y/N?  ")
        if confirm.upper() == "Y":
            print("SOLD. Enjoy the show, {}!".format(name))
            tickets_remaining -= num_tickets
        else:
            print("Sorry to see you go, {}. Hope to see you back soon!".format(name))
print("Sorry! We are sold out.")
