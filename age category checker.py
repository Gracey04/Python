age = int(input("Enter your age: "))

if age < 0:
    print("Baby")
elif age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("senior citizen")