# Day 2 - Employee List Processor

employees = [
    "Rahul",
    "Priya",
    "Anusha",
    "Lokesh"
]

# 1. Display employees
print("Employee List:")

for employee in employees:
    print(employee)


# 2. Search employee
search_name = input("\nEnter employee name to search: ")

found = False

for employee in employees:
    if employee.lower() == search_name.lower():
        print("Employee found:", employee)
        found = True
        break

if not found:
    print("Employee not found")


# 3. Count employees
print("\nTotal Employees:", len(employees))


# 4. Display employee numbers
print("\nEmployee Numbers:")

for number in range(len(employees)):
    print(number + 1, "-", employees[number])


# 5. Continue example
print("\nEmployee names with more than 4 characters:")

for employee in employees:
    if len(employee) <= 4:
        continue

    print(employee)


# 6. Nested loop example
print("\nNested Loop Example:")

for i in range(1, 3):
    for j in range(1, 3):
        print("i =", i, "j =", j)