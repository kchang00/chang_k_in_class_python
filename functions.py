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

# variables and scope
myNumberVariable = 10

# returning values from functions (very powerful)


def someMath(num1=2, num2=4):
    global myNumberVariable

    myNumberVariable = num1 + num2
    return num1 + num2


sum = someMath()
print("We are doing some math and getting", sum)

sum = someMath(10, 15)
print("another math operation with", sum, "as the result")
