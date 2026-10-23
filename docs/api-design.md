# HRMS API Design

## 1. Purpose

This document describes the Employee REST API implemented using Django,
Django REST Framework (DRF), and PostgreSQL.

## 2. REST API Fundamentals

- **API:** Application Programming Interface; allows software systems to communicate.
- **REST:** Representational State Transfer; an architectural style for APIs.
- **HTTP:** Protocol used for communication between clients and servers.
- **JSON:** Format used for sending structured request and response data.

### HTTP methods

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create a resource or perform an action |
| PUT | Replace/update a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

## 3. Base URL

Local development base URL:

`http://127.0.0.1:8000/api/employees/`

## 4. Authentication and Permissions

The global DRF settings configure:

- Session authentication
- Basic authentication
- `IsAuthenticated` as the default permission class

Clients must authenticate unless a view overrides these settings.

For production, use secure authentication practices and HTTPS. Avoid sending credentials over unencrypted connections.

## 5. Employee API Endpoints

| Method | Endpoint | Description | Success |
|---|---|---|---|
| GET | `/api/employees/` | List employees | 200 OK |
| POST | `/api/employees/` | Create employee | 201 Created |
| GET | `/api/employees/{id}/` | Retrieve employee | 200 OK |
| PUT | `/api/employees/{id}/` | Update employee | 200 OK |
| PATCH | `/api/employees/{id}/` | Partially update employee | 200 OK |
| DELETE | `/api/employees/{id}/` | Delete employee | 204 No Content |
| POST | `/api/employees/{id}/deactivate/` | Deactivate employee | 200 OK |

Replace `{id}` with the employee's numeric ID.

## 6. List, Search, and Filtering

### List employees

`GET /api/employees/`

The response is paginated.

### Search employees

`GET /api/employees/?search=Rahul`

Search checks employee code, first name, last name, and email.

### Active-only filtering

`GET /api/employees/?active_only=true`

Returns active employees only.

### Combine filters

`GET /api/employees/?search=Rahul&active_only=true`

Search and active-only filtering can be used together.

## 7. Pagination

The Employee API uses page-number pagination.

| Parameter | Description | Default / Limit |
|---|---|---|
| `page` | Select the page | Default page is 1 |
| `page_size` | Number of records per page | Default 10; maximum 100 |

Examples:

- `/api/employees/?page=1`
- `/api/employees/?page=2`
- `/api/employees/?page_size=20`
- `/api/employees/?page=1&page_size=20`

The paginated response contains `count`, `next`, `previous`, and `results`.

Example response structure:

```json
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/employees/?page=2",
  "previous": null,
  "results": []
}
```

The empty results array above is illustrative; actual employee records will be returned by the API.

## 8. Create an Employee

**Method:** POST

**Endpoint:** `/api/employees/`

Example JSON request:

```json
{
  "employee_code": "EMP101",
  "first_name": "Rahul",
  "last_name": "Kumar",
  "email": "rahul@example.com",
  "phone": "9876543210",
  "date_of_joining": "2026-10-01",
  "status": "Active",
  "department": 1
}
```

The department value must identify an existing active department.

Expected success status: `201 Created`.

The response includes employee fields and read-only `department_details`.

Example response:

```json
{
  "id": 101,
  "employee_code": "EMP101",
  "first_name": "Rahul",
  "last_name": "Kumar",
  "email": "rahul@example.com",
  "phone": "9876543210",
  "date_of_joining": "2026-10-01",
  "status": "Active",
  "department": 1,
  "department_details": {
    "id": 1,
    "name": "IT",
    "status": "Active"
  }
}
```

The IDs and department data above are illustrative.

## 9. Retrieve and Update an Employee

### Retrieve

`GET /api/employees/101/`

Returns the employee and department details when the employee exists.

### Full update

`PUT /api/employees/101/`

Send the complete set of required writable fields.

### Partial update

`PATCH /api/employees/101/`

Send only the fields that need to change.

Successful retrieval and updates return `200 OK`.

A nonexistent employee returns `404 Not Found`.

## 10. Deactivate an Employee

**Method:** POST

**Endpoint:** `/api/employees/101/deactivate/`

The endpoint changes the employee status to `Inactive`.

Successful deactivation returns `200 OK` with the employee representation.

Deactivating an already inactive employee leaves it inactive.

## 11. Delete an Employee

**Method:** DELETE

**Endpoint:** `/api/employees/101/`

An active employee cannot be deleted. Deactivate the employee first.

Successful deletion returns `204 No Content`, with no response body.

Deletion may be rejected if related records protect the employee.

## 12. Validation and Error Responses

The serializer validates employee codes, names, email addresses, phone numbers, and department status.

Examples of validation rules:

- Employee code must not be empty or duplicated.
- First and last names must not be empty.
- Email must not be empty or duplicated.
- Phone numbers must contain digits only when supplied.
- Employees can only be assigned to active departments.
- Inactive employees cannot be reactivated through the normal update API.
- Active employees cannot be deleted directly.

Example validation error:

```json
{
  "email": [
    "An employee with this email already exists."
  ]
}
```

Exact error wording and response structure depend on the validation rule that fails.

## 13. Common HTTP Status Codes

| Status | Meaning |
|---|---|
| 200 | Request succeeded |
| 201 | Resource created |
| 204 | Resource deleted |
| 400 | Invalid input or rejected operation |
| 401 | Authentication required or failed |
| 403 | Permission denied |
| 404 | Resource not found |

## 14. Query Efficiency

The employee search service uses:

`select_related("department")`

This loads the employee and its related department efficiently for serializer access.

Other implemented optimizations include:

- Filtering in the database using ORM querysets.
- Searching with Django `Q` conditions.
- Ordering employee results by employee code.
- Limiting list results through pagination.

Query performance should be measured with representative data before claiming specific performance improvements.

## 15. Automated Testing and Verification

Run the complete Django test suite:

```powershell
python manage.py test
```

Check project configuration:

```powershell
python manage.py check
```

Check whitespace errors in Git changes:

```powershell
git diff --check
```

## 16. Current Scope and Limitations

This document covers the Employee REST API.

The HTML employee pages are separate routes under `/employees/`.

Department information is exposed through the employee serializer. Separate department REST endpoints are not registered in the current project-level API URL configuration.

Review permissions, authentication behavior, and API responses against the running application whenever the implementation changes.

## 15. Automated Testing and Verification

### Run the test suite

Run the complete Django test suite:

```powershell
python manage.py test

Make sure the closing triple backticks are present immediately after `python manage.py test`.

Your file should have this structure:

1. `## 15. Automated Testing and Verification`
2. `### Run the test suite` with its properly closed code block.
3. `### Employee Role-Based Access`
4. `### Permission Design Decisions`
5. `### Verification Steps`
6. `### Known Limitations`

Keep the role-permission content you already added; just correct the code-block boundary and preserve the existing sections.

## Step 2 — Verify the Markdown

Save the file, then run:

```powershell
Get-Content .\docs\api-design.md | Select-Object -Last 55
git diff --check
git diff -- docs/api-design.md
### Employee Role-Based Access

The Employee API uses authentication and role-based permissions to restrict access to employee records.

| Role | Access |
|---|---|
| Admin | Full access to permitted Employee API operations |
| HR | Can create, read, and update employee records; cannot delete records |
| Manager | Read-only access to employee records |
| Employee | Can access their own linked employee record only |

Permission checks are applied at the API view level. Object-level permission checks are also performed for individual employee records, including detail and deactivate operations.

Employee list results are filtered by role. Regular Employees receive only their own linked employee record, while Admin, HR, and Manager roles can access the employee list according to their permissions.

### Permission Design Decisions

- Authentication is required by default through Django REST Framework.
- Role permissions are implemented using a custom permission class.
- Object-level checks help prevent users from accessing another employee's record.
- The employee list is filtered at the queryset level to restrict which records are returned.
- Permission behavior is verified through automated API tests, including forbidden operations and access to another employee's record.

### Verification Steps

Activate the project's virtual environment and run these commands from the repository root:

```powershell
python manage.py check
python manage.py test
git diff --check
```

Review the test output and Git changes before committing. The test suite should pass before changes are pushed.

### Known Limitations

- This document covers the Employee REST API; separate Department REST endpoints are not registered in the current project-level API URL configuration.
- Role permissions depend on the application's configured Django groups and user-to-employee relationships.
- Session and Basic authentication are configured for the current project. Production authentication and deployment security require separate review.
- Permission behavior should be retested whenever role rules, API views, or employee relationships change.