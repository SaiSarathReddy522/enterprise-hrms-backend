# Employee Management System - Mini System Design

## 1. System Overview

The Employee Management System is an HRMS module used to manage employee information and departments.

The system provides REST APIs through a Django backend and stores data in PostgreSQL.

---

# 2. Requirements

## Functional Requirements

The system should allow authorized users to:

1. Create employees.
2. View employees.
3. View an employee by ID.
4. Update employees.
5. Partially update employees.
6. Delete employees.
7. Create departments.
8. View departments.
9. View a department by ID.
10. Update departments.
11. Delete departments.

## Non-Functional Requirements

The system should provide:

- Security
- Reliability
- Scalability
- Maintainability
- Good performance
- Data consistency
- API validation
- Error handling

---

# 3. Actors

The main actors are:

| Actor | Responsibility |
|---|---|
| Admin | Manage employees and departments |
| HR | Manage employee information |
| Manager | View employee information |
| Employee | View own information |
| IT Support | Support system operations |
| Auditor | Review system activities |

---

# 4. Modules

The Employee Management System contains:

```text
Employee Management
Department Management
Authentication
Authorization
Employee Search
Employee Status Management
Audit Logging
Notification