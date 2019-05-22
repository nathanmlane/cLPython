def packer(**kwargs):
    print(kwargs)

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Who the f** are you?")

packer(name="gary", num=42, farts=None)
unpacker(**{"first_name": "gary", "last_name": "gary"})


def courses(teachers):
    course_list = []
    for value in teachers.values():
        course_list += value #why not append?
    return
