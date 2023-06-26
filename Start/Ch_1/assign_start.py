# Example file for Advanced Python: Language Features by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
X = 5
print(X)

# TODO: the assignment operator is part of an expression
# the_str = input("Enter a string: ")
# while the_str != "quit":
#     print("You entered: ", the_str)
#     the_str = input("Enter a string: ")

# TODO: The assignment expression is useful for writing concise code
# Do the same thing with the walrus operator
while (the_str := input("Enter a string: ")) != "quit":
    print("You entered: ", the_str)

# TODO: The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": len(values),
    "total": sum(values),
    "average": sum(values) / len(values)
}
# pprint.pp(val_data)

# TODO: The walrus operator can help make code more efficient
val_data2 = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s / l
}

pprint.pp(val_data2)
