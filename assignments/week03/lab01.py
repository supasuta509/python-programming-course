# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int (input("Enter age:"))
if age >= 60:
    print("age: Senior")
elif age >= 20 and age <=59  :  
    print("age: Adult")
elif age >= 13 and age <= 19 :
    print("age: Teenager")
else:
    print("age: Child")