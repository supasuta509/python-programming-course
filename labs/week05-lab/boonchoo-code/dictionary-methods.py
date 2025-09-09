# Sample data
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96, "Eve": 89}

# Length and membership 
print(f"Number of students: {len(scores)}")  # 5
print(f"Is Alice in scores? {'Alice' in scores}") #Ture
print(f"Is 'Frank' in scores? {'Frank' in scores}")

# Getting keys, values, items
print(f"Students: {list(scores.keys())}")
print(f"Scores: {list(scores.values())}")#หยิบตัวเลขออกมา
print(f"All data: {list(scores.items())}")#พ่น item ทั้งหมด ที่เป็นสมาชิก 

# Iterating through dictionary 
print("\nAll students and scores:")
for name, score in scores.items(): #คู่ของ
    print(f"{name}: {score}")

print("\nJust the names:")
for name in scores.keys():
    print(name)

print("\nJust the scores:")
for score in scores.values():
    print(score)

# Dictionary comprehension for filtering
high_scores = {name: score for name, score in scores.items() if score >= 90} # ตัวแปรscore  กรองคนที่มี่คะแนน มากกว่า 
print(f"High scores (>=90): {high_scores}")

# Finding min/max #maxหยิบชื่อและคะแนน ไอเท่ม ที่มีคะแนนมากที่สุดออกมา เก็บ minน้อยที่สุด เก็บ
best_student = max(scores, key=scores.get)
worst_student = min(scores, key=scores.get)
print(f"Best student: {best_student} with {scores[best_student]}")
print(f"Lowest score: {worst_student} with {scores[worst_student]}")

# fromkeys() method
subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0)   #สร้าง dictขึ้นมา
print(f"Default scores: {default_scores}")

# setdefault() method #กำหนดค่าเริ่มต้นของ key
student_grades = {}
student_grades.setdefault("Alice", []).append(85)
student_grades.setdefault("Alice", []).append(92)
student_grades.setdefault("Bob", []).append(78)
print(f"Student grades: {student_grades}")

