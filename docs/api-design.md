# HRMS API Design

## 1. REST API Fundamentals

### API

API stands for Application Programming Interface.

An API allows two software systems to communicate with each other.

Example:

Web Application → API → Django Backend → Database

---

### REST

REST stands for Representational State Transfer.

REST is an architectural style used to design web APIs.

REST APIs commonly use HTTP methods such as:

- GET
- POST
- PUT
- PATCH
- DELETE

---

### HTTP

HTTP stands for HyperText Transfer Protocol.

HTTP is used for communication between client and server.

Example:

Client → HTTP Request → Server

Server → HTTP Response → Client

---

### Request

A request is sent by the client to the server.

A request can contain:

- URL
- HTTP method
- Headers
- Request body
- Parameters

Example:

```http
POST /api/employees/

## Employee REST API Endpoints

Base URL: `/api/employees/`

### Authentication
All Employee API endpoints require an authenticated user.

### 1. List Employees
- Method: GET
- Endpoint: `/api/employees/`
- Success: `200 OK`

Query parameters:
- `search`: Search by employee code, first name, last name, or email.
- `active_only=true`: Return only active employees.

Example: `/api/employees/?search=Test`

### 2. Create Employee
- Method: POST
- Endpoint: `/api/employees/`
- Success: `201 Created`
- Invalid input: `400 Bad Request`

Example request:

```json
{
  "employee_code": "EMP101",
  "first_name": "Rahul",
  "last_name": "Kumar",
  "email": "rahul@example.com",
  "phone": "9876543210",
  "date_of_joining": "2026-10-01",
  "department": 1
}
```

The department ID must refer to an existing department.

### 3. Retrieve Employee
- Method: GET
- Endpoint: `/api/employees/{id}/`
- Success: `200 OK`
- Not found: `404 Not Found`

### 4. Update Employee
- Method: PUT
- Endpoint: `/api/employees/{id}/`
- Success: `200 OK`
- Invalid input: `400 Bad Request`

### 5. Partially Update Employee
- Method: PATCH
- Endpoint: `/api/employees/{id}/`
- Success: `200 OK`

### 6. Deactivate Employee
- Method: POST
- Endpoint: `/api/employees/{id}/deactivate/`
- Success: `200 OK`

Changes the employee status to `Inactive`.

### 7. Delete Employee
- Method: DELETE
- Endpoint: `/api/employees/{id}/`
- Success: `204 No Content`

Active employees cannot be deleted. Deactivate the employee first.

### Common HTTP Status Codes

| Status | Meaning |
|---|---|
| 200 | Request succeeded |
| 201 | Resource created |
| 204 | Resource deleted |
| 400 | Validation error |
| 401 or 403 | Authentication or permission denied |
| 404 | Resource not found |

### Run Automated Tests

```powershell
python manage.py test
```
