# HRMS ER Diagram

## Basic HRMS Relationships

```mermaid
erDiagram

    DEPARTMENT ||--o{ EMPLOYEE : contains
    EMPLOYEE ||--o{ ATTENDANCE : has
    EMPLOYEE ||--o{ LEAVE : requests
    EMPLOYEE ||--o{ PAYROLL : receives

    DEPARTMENT {
        int id PK
        varchar name
        text description
    }

    EMPLOYEE {
        int id PK
        varchar employee_code UK
        varchar name
        varchar email
        varchar phone
        int department_id FK
        date joining_date
        varchar status
    }

    ATTENDANCE {
        int id PK
        int employee_id FK
        date attendance_date
        time check_in
        time check_out
        varchar status
    }

    LEAVE {
        int id PK
        int employee_id FK
        varchar leave_type
        date start_date
        date end_date
        text reason
        varchar status
    }

    PAYROLL {
        int id PK
        int employee_id FK
        decimal basic_salary
        decimal hra
        decimal allowance
        decimal deductions
        decimal gross_salary
        decimal net_salary
        date payment_date
    }