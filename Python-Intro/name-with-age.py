def name_with_age(name : str , age: int):
    name_with = name.title() + " is " + str(age) + " years old."
    return name_with
print(name_with_age("alice", 30))