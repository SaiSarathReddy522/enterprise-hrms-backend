# Day 2 - Python Collections
# HRMS Employee Management

employees = []

# Employee data
employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 30000,
    "status": "Active"
}


# 1. Add employee
employees.append(employee)

print("Employee added successfully")


# 2. Display employees
print("\nEmployee List:")

for emp in employees:
    print(emp)


# 3. Update employee
for emp in employees:
    if emp["id"] == 101:
        emp["salary"] = 35000
        emp["department"] = "Development"

print("\nEmployee after update:")

for emp in employees:
    print(emp)


# 4. Search employee
search_id = 101

print("\nSearch Employee:")

for emp in employees:
    if emp["id"] == search_id:
        print("Employee found:", emp)
        break


# 5. Delete employee
employees = [
    emp for emp in employees
    if emp["id"] != 101
]

print("\nEmployee List after delete:")

for emp in employees:
    print(emp)


# Collection examples

# List
employee_names = ["Rahul", "Priya", "Anusha", "Lokesh"]

# Tuple
departments = ("IT", "HR", "Finance", "Sales")

# Set
unique_departments = {"IT", "HR", "IT", "Finance"}

# Dictionary
employee_details = {
    "id": 102,
    "name": "Priya",
    "department": "HR"
}

print("\nList:", employee_names)
print("Tuple:", departments)
print("Set:", unique_departments)
print("Dictionary:", employee_details)