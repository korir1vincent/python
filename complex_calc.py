p = int(input("Enter the first input: "))
q = int(input("Enter the second input: "))

oper = input("Enter the type of operation you want to perform (+, -, *, /, %): ")

result = 0
if oper == "+":
    result = p+q
elif oper == "-":
    result = p-q
elif oper == "*":
    result = p*q
elif oper == "/":
    result = p//q # Integer Division
elif oper == "%":
    result = p%q
else:
    print("Invalid Input")
print("Your answer is: ",result)