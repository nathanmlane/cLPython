shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    print("Great! We'll grab some {}. That makes our total list come to {} items.".format(item, len(shopping_list)))

def show_help():
    print("What should we pickup at the store?")
    print("""
Enter 'DONE' to complete your list.
Enter 'VIEW' to see your list.
Enter 'HELP' to show the help menu.
""")

def show_list():
    print("This is what we're getting:")
    for item in shopping_list:
        print("* " + item)

show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == "DONE":
        show_list()
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "VIEW":
        show_list()
        continue

    add_to_list(new_item)
