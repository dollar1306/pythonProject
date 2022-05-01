def print_message(value):
    try:
        message = value + " - OK"
        print("No problem, just print the message...")
        print(message)
    except TypeError:
        print("You should know, there was a type error in your program, but I fixed it...")
        message = str(value) + " - OK"
        print(message)



value = 123 #"Hello"
print_message(value)