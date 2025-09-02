"""
Personal Finance Calculator
Student: [supasuta thimtong]
Date: [25/07/2025]
Purpose: Calculate monthly budget and savings
""" 
#ขอข้อมูลรายได้และรายจ่ายจากผู้ใช้
try:
     monthly_income = float(input("Enter your monthly income (THB): "))
     rent_cost = float(input("Enter your monthly rent/housing cost (THB): "))
     food_budget = int(input("Enter your monthly food budget (THB): "))
     transportation_cost = float(input("Enter your monthly transportation cost (THB): "))
     entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))
     emergency_fund_percent = float(input("Enter emergency fund saving percent (e.g., 10.5): "))
     investment_percent = float(input("Enter investment percent (e.g., 15.0): "))
except ValueError:
 print("Invalid input. Please enter numbers only.")
 #ตรวจสอบความถูกต้องของข้อมูล
if monthly_income <= 0:
     print("Income must be greater than 0.")

if any(x < 0 for x in [rent_cost, food_budget, transportation_cost, entertainment_budget, emergency_fund_percent, investment_percent]):
     print("Values cannot be negative.")
#คำนวณค่าใช้จ่ายคงที่ = ค่าเช่า + ค่าเดินทาง
fixed_expenses = rent_cost + transportation_cost
#คำนวณค่าใช้จ่ายไม่คงที่ = ค่าอาหาร + บันเทิง
variable_expenses = food_budget + entertainment_budget
#คำนวณค่าใช้จ่ายทั้งหมด
total_expenses = fixed_expenses + variable_expenses
#รายไดเคงเหลือก่อนออมและลงทุน
remaining_income = monthly_income - total_expenses
 #เงินฉุกเฉิน
emergency_fund = (emergency_fund_percent / 100) * monthly_income
#เงินลงทุน
investment = (investment_percent / 100) * monthly_income
#เงินเหลือสำหรับออม
available_savings = remaining_income - emergency_fund - investment

# อัตราค่าใช้จ่ายทั้งหมด
expense_ratio = (total_expenses / monthly_income) * 100
# แสดงผลลัพะ์
print("\n===== Monthly Budget Summary =====")
print(f"Total Fixed Expenses      : {fixed_expenses:.2f} THB")
print(f"Total Variable Expenses   : {variable_expenses:.2f} THB")
print(f"Total Expenses            : {total_expenses:.2f} THB")
print(f"Remaining Income          : {remaining_income:.2f} THB")
print(f"Emergency Fund Amount     : {emergency_fund:.2f} THB")
print(f"Investment Amount         : {investment:.2f} THB")
print(f"Available For Savings     : {available_savings:.2f} THB")
print(f"Expense Ratio             : {expense_ratio:.2f}%")
#แจ้งเตือนหากรายได้เกิน
if available_savings < 0:
    print("\nWarning: Your expenses and savings exceed your income.") 
    print("Suggestion: Try reducing your spending or saving a lower percentage.") 