

# HRMS Database Design

## 1. Database Overview

The HRMS (Human Resource Management System) database stores and manages
employee, department, attendance, leave, payroll, and user information.

The database follows relational database design principles.

---

## 2. User Table

The User table stores system user login and role information.

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| username | VARCHAR | Unique username |
| email | VARCHAR | User email |
| password_hash | VARCHAR | Hashed password |
| role | VARCHAR | User role |
| status | VARCHAR | User status |
| created_at | TIMESTAMP | Account creation time |

### Primary Key

`id`

### Constraints

- `username` should be UNIQUE.
- `email` should be UNIQUE.
- `password_hash` should be NOT NULL.
- `status` can store values such as Active or Inactive.

---

## 3. Department Table

The Department table stores information about company departments.

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| name | VARCHAR | Department name |
| description | TEXT | Department description |

### Primary Key

`id`

### Constraints

- `name` should be NOT NULL.
- `name` should be UNIQUE.

### Example

| id | name | description |
|---|---|---|
| 1 | IT | Information Technology |
| 2 | HR | Human Resources |
| 3 | Finance | Finance Department |

---

## 4. Employee Table

The Employee table stores employee personal and employment information.

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| employee_code | VARCHAR | Unique employee code |
| name | VARCHAR | Employee name |
| email | VARCHAR | Employee email |
| phone | VARCHAR | Employee phone number |
| department_id | INTEGER | Foreign Key |
| joining_date | DATE | Employee joining date |
| status | VARCHAR | Employee status |

### Primary Key

`id`

### Foreign Key

`department_id` references `Department(id)`.

### Constraints

- `employee_code` should be UNIQUE.
- `name` should be NOT NULL.
- `email` should be UNIQUE.
- `department_id` should reference a valid department.
- `status` can contain values such as Active or Inactive.

### Example

| id | employee_code | name | email | department_id | status |
|---|---|---|---|---|---|
| 101 | EMP001 | Rahul | rahul@example.com | 1 | Active |
| 102 | EMP002 | Priya | priya@example.com | 2 | Active |

---

## 5. Attendance Table

The Attendance table stores daily attendance records of employees.

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| employee_id | INTEGER | Foreign Key |
| attendance_date | DATE | Attendance date |
| check_in | TIME | Employee check-in time |
| check_out | TIME | Employee check-out time |
| status | VARCHAR | Attendance status |

### Primary Key

`id`

### Foreign Key

`employee_id` references `Employee(id)`.

### Constraints

- `employee_id` should reference a valid employee.
- `attendance_date` should be NOT NULL.
- `status` can contain values such as Present, Absent, or Leave.

### Example

| id | employee_id | attendance_date | check_in | check_out | status |
|---|---|---|---|---|---|
| 1 | 101 | 2026-10-01 | 09:30 | 18:00 | Present |
| 2 | 102 | 2026-10-01 | 09:45 | 18:10 | Present |

---

## 6. Leave Table

The Leave table stores employee leave requests and their approval status.

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| employee_id | INTEGER | Foreign Key |
| leave_type | VARCHAR | Type of leave |
| start_date | DATE | Leave start date |
| end_date | DATE | Leave end date |
| reason | TEXT | Reason for leave |
| status | VARCHAR | Leave request status |

### Primary Key

`id`

### Foreign Key

`employee_id` references `Employee(id)`.

### Constraints

- `employee_id` should reference a valid employee.
- `leave_type` should be NOT NULL.
- `start_date` should be NOT NULL.
- `end_date` should be NOT NULL.
- `status` can contain values such as Pending, Approved, or Rejected.

### Example

| id | employee_id | leave_type | start_date | end_date | status |
|---|---|---|---|---|---|
| 1 | 101 | Casual Leave | 2026-10-05 | 2026-10-06 | Pending |
| 2 | 102 | Sick Leave | 2026-10-07 | 2026-10-07 | Approved |

---

## 7. Payroll Table

The Payroll table stores employee salary and payment information.

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| employee_id | INTEGER | Foreign Key |
| basic_salary | DECIMAL | Basic salary |
| hra | DECIMAL | House Rent Allowance |
| allowance | DECIMAL | Other allowances |
| deductions | DECIMAL | Salary deductions |
| gross_salary | DECIMAL | Gross salary |
| net_salary | DECIMAL | Net salary |
| payment_date | DATE | Salary payment date |

### Primary Key

`id`

### Foreign Key

`employee_id` references `Employee(id)`.

### Constraints

- `employee_id` should reference a valid employee.
- `basic_salary` should be NOT NULL.
- Salary values should not be negative.
- `net_salary` should represent the final salary after deductions.

### Salary Calculation

```text
Gross Salary = Basic Salary + HRA + Allowance

Net Salary = Gross Salary - Deductions

---

## 8. Database Relationships

### Department → Employee

One department can have many employees.

```text
Department (1) ───────── (N) Employee