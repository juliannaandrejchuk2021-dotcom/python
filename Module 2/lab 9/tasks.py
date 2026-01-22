import math,random

print("=========Task 1=========")
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
operator=input("Enter an operator (+, -, *, /,pow,mod,div): ")
result=0
try:
    if operator=='+':
        result=a+b
    elif operator=='-':
        result=a-b
    elif operator=='*':
        result=a*b
    elif operator=='/':
        result=a/b
    elif operator=='pow':
        result=a**b
    elif operator=='mod':
        result=a%b
    elif operator=='div':
        result=a//b
    else:
        print("Invalid operator")
        result=None
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    if result is not None:
        print("Result:", result)
finally:
    pass
print("=========Task 2=========")
print("Leap Year Checker")

try:
    year=int(input("Enter a year: "))
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
try:
    n = random.randint(-100, 1100)

    if n < 100 or n > 999:
        raise ValueError("Number is not three-digit")

    print(f"Random number: {n}")

    result = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        result += digit
        temp //= 10

    print(f"Sum of digits: {result}")

except ValueError as e:
    print("Error:", e)
print("=========Task 3=========")
def Factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n*Factorial(n-1)


num=int(input("Enter a non-negative integer: "))
try:
        print(f"Factorial of {num} is {Factorial(num)}")
except RecursionError:
        print("Invalid input. Please enter a non-negative integer.")


      
    

