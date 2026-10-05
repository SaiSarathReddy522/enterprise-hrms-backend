# Django Backend Architecture

## 1. Overview

Django is a Python web framework used to build backend applications.

In the Enterprise HRMS project, Django will be used for URL routing, application logic, database operations, and HTTP responses.

## 2. Django MVT Architecture

Django follows the Model-View-Template architecture.

### Model

The Model represents application data and communicates with the database using Django ORM.

Example:

```text
Employee
- id
- name
- department
- salary
- status
```

### View

The View receives HTTP requests, executes application logic, communicates with models or services, and returns a response.

### Template

The Template is responsible for presenting data to the user through HTML.

### URL Routing

URL routing maps incoming requests to the appropriate Django view.

## 3. Request-Response Cycle

```text
Client
  ↓
URL
  ↓
View
  ↓
Model / Business Logic
  ↓
Database
  ↓
Response
```

For an HRMS employee request:

```text
Client
  ↓
GET /employees/
  ↓
Django URL
  ↓
Employee View
  ↓
Business Logic
  ↓
Django ORM
  ↓
PostgreSQL
  ↓
Employee Data
  ↓
HTTP Response
```

## 4. System Design Mapping

| System Layer      | Django Component   |
| ----------------- | ------------------ |
| Client Layer      | Browser / Frontend |
| Routing Layer     | urls.py            |
| Application Layer | Views / Services   |
| Data Access Layer | Django ORM         |
| Database Layer    | PostgreSQL         |

## 5. Important Django Files

### manage.py

`manage.py` is the command-line utility used to manage the Django project.

Common commands:

```bash
python manage.py runserver
python manage.py startapp
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

### config/settings.py

Contains project configuration such as installed applications, middleware, database configuration, templates, and other Django settings.

### config/urls.py

Contains the main URL routing configuration for the Django project.

### config/asgi.py

Provides the ASGI entry point for asynchronous web servers.

### config/wsgi.py

Provides the WSGI entry point for traditional Python web servers.

## 6. HRMS Architecture

The Enterprise HRMS backend will follow a modular architecture:

```text
Client
   ↓
Django URL Router
   ↓
Application / API Layer
   ↓
Business Logic
   ↓
Django ORM
   ↓
PostgreSQL
```

Future HRMS modules include:

* Employee Management
* Department Management
* Attendance
* Leave
* Payroll
* Recruitment
* Performance
* Documents
* Assets
* Projects
* Notifications
* Reports
* Audit Logs

## 7. Separation of Responsibilities

Each layer should have a clear responsibility.

```text
Presentation → API / Response
Application  → Business Logic
Data Access  → ORM
Database     → Persistent Data
```

## 8. Key Principle

The backend should be modular so that each module has a clear responsibility.

For example:

```text
Employee Module
      ↓
Employee Business Logic
      ↓
Django ORM
      ↓
Employee Database Tables
```

This separation makes the HRMS backend easier to maintain, test, and extend.
