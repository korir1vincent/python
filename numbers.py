#numbers greater or smaller
num=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
num3=int(input("Enter your third number:"))
num4=int(input("Enter your fourth number:"))

if num>num2 and num>num3 and num>num4:
    print(f"{num} is greater than {num2,num3,num4}")
elif num<num2 and num<num3 and num<num4:
    print(f"{num} is smaller than {num2,num3,num4}")
if num2>num and num2>num3 and num2>num4:
    print(f"{num2} is greater than {num,num3,num4}")
elif num2<num and num2<num3 and num2<num4:
    print(f"{num2} is smaller than {num,num3,num4}")
if num3>num and num3>num2 and num3>num4:
    print(f"{num3} is greater than {num,num2,num4}")
elif num3<num and num3<num2 and num3<num4:
    print(f"{num3} is smaller than {num,num2,num4}")
if num4>num and num4>num2 and num4>num:
    print(f"{num4} is greater than {num,num2,num3}")
elif num4<num and num4<num2 and num4<num3:
    print(f"{num4} is smaller than {num,num2,num3}")

