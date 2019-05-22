def packer(**kwargs):
    print(kwargs)

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Who the f** are you?")

packer(name="gary", num=42, farts=None)
unpacker(**{"first_name": "gary", "last_name": "gary"})


course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long.".format(course, minutes))
