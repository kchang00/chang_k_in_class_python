# block of statements
# Python prefers spaces as indentation, can change at bottom by spaces
# Functions and classes need 2 spaces after each


def greetings():
    print("Hello from the greetings function")


# the greetings function just says hello
# invoke or call the function
greetings()

# only the internal statements understand what the variable means


def greetingsWithArgs(msg="a default message"):
    print("now we're saying", msg, "from another function")

# similar to placeholder variables


greetingsWithArgs("Hey! 'Sup!")
greetingsWithArgs("Something completely different")
greetingsWithArgs("Running yet again!")
