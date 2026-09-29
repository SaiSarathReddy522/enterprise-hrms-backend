# HRMS Requirements

## 1. Introduction

The Human Resource Management System (HRMS) is a backend system used to manage employee-related activities such as authentication, employees, departments, attendance, leave, payroll, recruitment, assets, performance, notifications, reports, and audit logs.

This document defines the Functional Requirements (FR) and Non-Functional Requirements (NFR) for the HRMS.

---

# 2. Authentication

## Functional Requirements

- The system shall allow users to register.
- The system shall allow users to login using valid credentials.
- The system shall validate username/email and password.
- The system shall allow users to logout.
- The system shall allow users to reset their password.
- The system shall provide role-based access to users.
- The system shall prevent unauthorized users from accessing protected resources.

## Non-Functional Requirements

- Passwords shall be stored securely using hashing.
- Authentication requests should be processed efficiently.
- The authentication system shall be available to authorized users.
- User sessions or tokens shall be handled securely.

---

# 3. Employee Management

## Functional Requirements

- HR shall be able to create an employee.
- HR shall be able to view employee details.
- HR shall be able to update employee details.
- HR shall be able to deactivate an employee.
- Authorized users shall be able to search employees.
- The system shall maintain employee identification details.
- The system shall maintain employee department information.
- The system shall maintain employee status.

## Non-Functional Requirements

- Employee data shall be protected from unauthorized access.
- Employee records shall be stored reliably.
- Employee search should provide results efficiently.
- The system shall support a large number of employee records.

---

# 4. Department Management

## Functional Requirements

- HR/Admin shall be able to create departments.
- HR/Admin shall be able to update departments.
- HR/Admin shall be able to view departments.
- HR/Admin shall be able to deactivate departments.
- The system shall assign employees to departments.
- The system shall display employees belonging to a department.

## Non-Functional Requirements

- Department data shall maintain consistency.
- Department information shall be available to authorized users.
- Department operations should perform efficiently.

---

# 5. Attendance

## Functional Requirements

- Employees shall be able to check in.
- Employees shall be able to check out.
- The system shall record attendance date and time.
- Employees shall be able to view their attendance.
- Managers/HR shall be able to view employee attendance.
- HR shall be able to generate attendance reports.
- The system shall maintain attendance history.

## Non-Functional Requirements

- Attendance records shall be stored accurately.
- Attendance data shall be protected.
- The system should handle multiple attendance requests.
- Attendance information should be available reliably.

---

# 6. Leave Management

## Functional Requirements

- Employees shall be able to apply for leave.
- Employees shall be able to view their leave requests.
- Managers shall be able to approve or reject leave requests.
- HR shall be able to view leave records.
- The system shall maintain leave balances.
- The system shall maintain leave history.
- The system shall notify employees about leave approval or rejection.

## Non-Functional Requirements

- Leave data shall be stored consistently.
- Only authorized users shall approve or reject leave.
- Leave operations should respond quickly.
- Leave records shall be available reliably.

---

# 7. Payroll

## Functional Requirements

- HR/Finance shall be able to create salary records.
- The system shall store employee salary information.
- The system shall calculate salary components.
- The system shall maintain deductions.
- The system shall maintain allowances.
- The system shall generate payroll records.
- Authorized users shall be able to view payroll information.
- The system shall generate payroll reports.

## Non-Functional Requirements

- Payroll information shall be highly secure.
- Payroll calculations shall be accurate.
- Payroll records shall be stored reliably.
- Only authorized users shall access salary information.

---

# 8. Recruitment

## Functional Requirements

- HR shall be able to create job openings.
- HR shall be able to update job openings.
- Candidates shall be able to submit applications.
- HR shall be able to view candidate applications.
- HR shall be able to update candidate status.
- The system shall maintain candidate information.
- The system shall maintain recruitment history.

## Non-Functional Requirements

- Candidate information shall be protected.
- Recruitment data shall be stored reliably.
- The system should support multiple job applications.
- Recruitment operations should perform efficiently.

---

# 9. Assets

## Functional Requirements

- IT/Admin shall be able to create asset records.
- IT/Admin shall be able to assign assets to employees.
- The system shall maintain asset details.
- The system shall track asset status.
- IT/Admin shall be able to update asset information.
- IT/Admin shall be able to return assets.
- The system shall maintain asset assignment history.

## Non-Functional Requirements

- Asset records shall be accurate.
- Asset information shall be accessible only to authorized users.
- Asset data shall be stored reliably.
- Asset search should perform efficiently.

---

# 10. Performance Management

## Functional Requirements

- Managers shall be able to create performance reviews.
- Managers shall be able to update performance reviews.
- Employees shall be able to view their performance results.
- The system shall maintain performance history.
- HR shall be able to view performance records.
- The system shall store performance ratings and feedback.

## Non-Functional Requirements

- Performance information shall be confidential.
- Performance records shall be stored securely.
- Authorized users should be able to access performance data efficiently.

---

# 11. Notifications

## Functional Requirements

- The system shall send notifications to users.
- The system shall notify employees about leave updates.
- The system shall notify users about important HR events.
- Users shall be able to view notifications.
- Users shall be able to mark notifications as read.

## Non-Functional Requirements

- Notifications should be delivered reliably.
- Notification processing should be efficient.
- The notification system should support multiple users.

---

# 12. Reports

## Functional Requirements

- HR shall be able to generate employee reports.
- HR shall be able to generate attendance reports.
- HR shall be able to generate leave reports.
- Finance shall be able to generate payroll reports.
- HR/Admin shall be able to generate department reports.
- Authorized users shall be able to view reports.

## Non-Functional Requirements

- Reports should be generated within a reasonable time.
- Report data shall be accurate.
- Reports shall be accessible only to authorized users.
- The system should support large datasets.

---

# 13. Audit Logs

## Functional Requirements

- The system shall record important user activities.
- The system shall record login activities.
- The system shall record data creation activities.
- The system shall record data update activities.
- The system shall record data deletion activities.
- Authorized users shall be able to view audit logs.
- The system shall maintain audit history.

## Non-Functional Requirements

- Audit logs shall be protected from unauthorized modification.
- Audit records shall be stored reliably.
- Audit information shall be secure.
- Audit logs should be searchable efficiently.

---

# 14. Summary

The HRMS shall provide the following major modules:

1. Authentication
2. Employee Management
3. Department Management
4. Attendance
5. Leave Management
6. Payroll
7. Recruitment
8. Assets
9. Performance Management
10. Notifications
11. Reports
12. Audit Logs

The Functional Requirements define what the HRMS should do.

The Non-Functional Requirements define qualities such as:

- Security
- Performance
- Availability
- Reliability
- Scalability
- Maintainability
- Data consistency

These requirements will be used as the foundation for the future HRMS system design and backend implementation.