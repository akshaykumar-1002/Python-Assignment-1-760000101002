# Q20. Calculate quotient and remainder of two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b != 0:
    print("Quotient =", a // b)
    print("Remainder =", a % b)
else:
    print("Division by zero is not allowed.")
