# Enterprise HRMS Backend

A Django-based backend for an Enterprise Human Resource Management System (HRMS), built with Python, Django REST Framework, and PostgreSQL.

## Technology Stack

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Django automated testing framework
- Git and GitHub

## Implemented Features

- Employee creation, retrieval, updating, deactivation, and deletion
- Employee search and active-status filtering
- Pagination with a configurable maximum page size
- Input validation and duplicate employee checks
- Authentication and role-based access controls
- Employee and department database relationships
- Database error handling and transaction rollback tests
- Automated API and permission tests

## Project Structure

```text
enterprise-hrms-backend/
├── apps/
│   ├── common/
│   ├── departments/
│   └── employees/
├── config/
├── docs/
├── evidence/
├── manage.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python compatible with the project dependencies
- PostgreSQL installed and running
- Git
- PowerShell on Windows

## Setup

### 1. Clone the repository

```powershell
git clone https://github.com/SaiSarathReddy522/enterprise-hrms-backend.git
cd enterprise-hrms-backend
```

### 2. Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks virtual-environment activation, use an approved execution-policy setting for your environment or run the virtual environment's Python executable directly.

## Environment Configuration

The application reads sensitive settings from environment variables. Configure these variables in the PowerShell session used to run Django.

### 1. Generate a Django secret key

```powershell
$env:DJANGO_SECRET_KEY = .\.venv\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. Enter the PostgreSQL password securely

```powershell
$securePassword = Read-Host "Enter PostgreSQL password" -AsSecureString
$pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($securePassword)

try {
    $env:HRMS_DB_PASSWORD = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer)
}
finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer)
    Remove-Variable securePassword, pointer -ErrorAction SilentlyContinue
}
```

### 3. Configure PostgreSQL

Configure PostgreSQL with the database and user expected by `config/settings.py`, or update the non-secret database settings to match your environment.

Default connection settings:

| Setting | Value |
|---|---|
| Database | `hrms_db` |
| User | `hrms_user` |
| Host | `127.0.0.1` |
| Port | `5432` |

The environment variables above apply only to the current PowerShell session. Set them again when starting a new session. Never commit passwords, secret keys, or other credentials.

## Database Setup and Startup

From the project root, after configuring the environment and database, run:

```powershell
python manage.py check
python manage.py migrate
python manage.py runserver
```

The development server normally runs at:

`http://127.0.0.1:8000/`

Use Django's development server only for development and testing, not as a production deployment server.

## Automated Testing and Validation

Run the complete test suite:

```powershell
python manage.py test
```

If you want to reuse the existing test database where supported:

```powershell
python manage.py test --keepdb
```

Run Django's system check:

```powershell
python manage.py check
```

Check whitespace and patch formatting:

```powershell
git diff --check
```

Review the current branch and working tree:

```powershell
git status
git log -5 --oneline
```

Recorded test and system-check evidence is available in the `evidence/` directory. Rerun the commands to confirm the results for the current code version.

## Application Routes

| Route | Purpose |
|---|---|
| `/admin/` | Django administration |
| `/employees/` | Employee HTML pages |
| `/departments/` | Department HTML pages |
| `/api/employees/` | List and create employees |
| `/api/employees/<id>/` | Retrieve, update, and delete an employee |
| `/api/employees/<id>/deactivate/` | Deactivate an employee |

The employee REST API supports search, active-status filtering, and pagination. See `docs/api-design.md` for endpoint details, request and response formats, validation rules, and permissions.

## Authentication and Permissions

The API requires authentication according to the configured Django REST Framework settings. Employee role permissions are implemented for the configured Admin, HR, Manager, and Employee groups.

Actual access depends on the permission rules, HTTP method, and object-level checks. Review the permission implementation and automated tests before changing access rules.

## Documentation

- `docs/requirements.md` — HRMS requirements
- `docs/system-design.md` — system design
- `docs/architecture.md` — system architecture overview
- `docs/django-architecture.md` — Django application architecture
- `docs/api-design.md` — API contracts and behavior
- `docs/api-flow.md` — request flow
- `docs/database-design.md` — database design
- `docs/hrms-er-diagram.md` — entity relationships
- `docs/recovery-runbook.md` — troubleshooting and recovery guidance

## Security Notes

- Keep `DJANGO_SECRET_KEY` and `HRMS_DB_PASSWORD` private.
- Do not commit `.env` files, passwords, access tokens, production data, or sensitive employee information.
- Use test data for automated testing and demonstrations.
- Verify authentication, role permissions, and object-level access controls.
- Review deployment settings before exposing the application outside a trusted development environment.
- Use environment-specific backup, recovery, monitoring, and production deployment procedures.

## Current Scope and Known Limitations

- The implemented REST API currently focuses on employee management.
- Department pages are available through HTML routes; a separate Department REST API is not currently registered in the main URL configuration.
- Other HRMS modules described in the requirements or design documents should not be considered implemented unless supported by application code and tests.
- Production deployment, monitoring, backups, and recovery require environment-specific configuration.
- Passing automated tests does not by itself establish production readiness.

## Git Validation

Check the current branch and working tree:

```powershell
git status
git log -5 --oneline
```

The repository is hosted at [SaiSarathReddy522/enterprise-hrms-backend](https://github.com/SaiSarathReddy522/enterprise-hrms-backend).
