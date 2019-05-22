import os

shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_list():
    clear_screen()
    print("This is what we're getting:")
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1
    print("-"*10)

def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press Enter to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0
    try:
            position = abs(int(position))
    except ValueError:
            position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)
    show_list()

def show_help():
    clear_screen()
    print("What should we pickup at the store?")
    print("""
Enter 'DONE' to complete your list.
Enter 'VIEW' to see your list.
Enter 'HELP' to show the help menu.
Enter 'REMOVE' to delete an item to your list.
""")

def remove_item():
    show_list()
    what_to_remove = input("What would you like to remove?\n ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        show_list()
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "VIEW":
        show_list()
        continue
    elif new_item.upper() == "REMOVE":
        remove_item()
        show_list()
        continue
    else:
        add_to_list(new_item)
