# HRMS Employee API Flow

## Overview

The HRMS Employee API follows this flow:

Client → API Endpoint → Serializer → View → Django ORM → Database

## 1. Client

The client sends an HTTP request to the HRMS API.

Examples:

- Postman
- Web application
- Mobile application
- Frontend application

## 2. API Endpoint

Employee API endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/employees/` | Get all employees |
| POST | `/api/employees/` | Create employee |
| GET | `/api/employees/{id}/` | Get employee by ID |
| PUT | `/api/employees/{id}/` | Fully update employee |
| PATCH | `/api/employees/{id}/` | Partially update employee |
| DELETE | `/api/employees/{id}/` | Delete employee |

## 3. Serializer

`EmployeeSerializer` is created using Django REST Framework's `ModelSerializer`.

File:

`apps/employees/serializers.py`

Responsibilities:

- Convert model objects into JSON
- Validate incoming data
- Check required fields
- Validate email data
- Convert validated data into model data
- Save validated data

The employee ID is read-only.

## 4. APIView

The APIView handles HTTP requests and responses.

File:

`apps/employees/views.py`

`EmployeeListCreateAPIView` handles:

- GET
- POST

`EmployeeDetailAPIView` handles:

- GET
- PUT
- PATCH
- DELETE

## 5. Django ORM

Django ORM provides communication between Python/Django and the database.

Examples:

```python
Employee.objects.all()
Employee.objects.get(pk=2)
employee.save()
employee.delete()