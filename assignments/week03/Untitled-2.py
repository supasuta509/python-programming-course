age = int (input("Enter age:"))
if age >= 60:
    print("age: Senior")
elif age >= 20 and age <= 59:
    print("age: Adult")
elif age >= 13 and age <= 19:
    print("age: Teenager")
else:
    print("age: Child")