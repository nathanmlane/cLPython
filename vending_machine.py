sodas = ["Dr. Pepper", "Coke", "Sprite",]
chips = ["Pretzels", "Lays", "Doritos",]
candy = ["Nerds", "Sour Patch Kids", "Snickers",]

while True:
    choice = input("Would you like any soda, chips, or candy? ").lower()

    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Please choose which you'd like.")
            continue
    except IndexError:
        print("Sorry. We're all out of {}.".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))
