#Functions dont work unless you call them
def myfunc():  #functions in python
    print("This is my function")
myfunc()
myfunc()
def addtwonumber():
    num=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print(f"The sum of {num} and {num2} is {num+num2}")
addtwonumber()
def calculator():
    p = int(input("Enter the first input: "))
    q = int(input("Enter the second input: "))

    oper = input("Enter the type of operation you want to perform (+, -, *, /, %): ")

    result = 0
    if oper == "+":
        result = p + q
    elif oper == "-":
        result = p - q
    elif oper == "*":
        result = p * q
    elif oper == "/":
        result = p // q  # Integer Division
    elif oper == "%":
        result = p % q
    else:
        print("Invalid Input")
    print("Your answer is: ", result)
calculator()