#Three numbers calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: " ))

print("Choose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - multiplication")
print("4 - Division")

choice = input("Enter your choice (1-4)")

if choice == "1":
    print("Result:", num1 + num2 + num3)
elif choice == "2":
    print("Result:", num1 - num2 - num3)
elif choice == "3":
    print("Result:", num1 * num2 * num3)
elif choice =="4":
    if num2 == 0 or num3 == 0:
        print(" cannot be divided by zero")
    else:
        print("Result:", num1/num2/num3)
else:
    print("invalid option")

