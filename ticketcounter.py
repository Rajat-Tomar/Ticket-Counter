SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining:
    print(f"There are {tickets_remaining} tickets remaining.")
    name = input("What is your name? ")

    try:
        num_tickets = int(input(f"How many tickets would you like to buy {name}? "))
        if num_tickets > tickets_remaining:
            raise ValueError(f"Sorry, we just have {tickets_remaining} tickets remaining!")
    except ValueError as err:
        print(f"Oh no! we ran into an issue, {err}, Please try again!")
    else:
        billed_amount = calculate_price(num_tickets)
        print(f'Your billed amount is ${billed_amount}')

    should_proceed = input(f"Do you want to proceed {name}? Y/N ")

    if should_proceed.upper() == "Y":
        print("SOLD!")
    else:
        print(f"Thank you anways {name}!")

print("We're sorry, the tickets are all sold out!")
