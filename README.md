# Enterprise HRMS Backend

A Django-based backend for an Enterprise Human Resource Management System (HRMS).

## Technology Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Automated tests using Django's test framework

## Implemented Features

- Employee create, retrieve, update, deactivate and delete operations
- Employee search and active-status filtering
- Pagination with a maximum page size
- Input validation and duplicate employee checks
- Authentication and role-based access controls
- Department and employee database relationships
- Database error handling and transaction rollback tests

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

- A compatible Python version
- PostgreSQL installed and running
- Git
- PowerShell on Windows (commands below use PowerShell)

## Setup

Clone the repository and enter its root directory:

```powershell
git clone <YOUR_REPOSITORY_URL>
cd enterprise-hrms-backend
```

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Environment Configuration

The application reads sensitive configuration from environment variables.

Set a Django secret key for the current PowerShell session:

```powershell
$env:DJANGO_SECRET_KEY = .\.venv\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Enter the PostgreSQL password without displaying it as you type:

```powershell
$securePassword = Read-Host "Enter PostgreSQL password" -AsSecureString
$pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($securePassword)
try {
    $env:HRMS_DB_PASSWORD = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer)
}
finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer)
}
```

Configure PostgreSQL with the database and user expected by
`config/settings.py`, or update the non-secret database settings to match
your environment. The default connection settings are:

- Database: `hrms_db`
- User: `hrms_user`
- Host: `127.0.0.1`
- Port: `5432`

The environment variables above are session-specific. Set them again
when opening a new PowerShell session. Never commit secrets or passwords.

## Database and Startup

Run these commands from the project root after configuring the environment:

```powershell
python manage.py check
python manage.py migrate
python manage.py runserver
```

The development server normally runs at `http://127.0.0.1:8000/`.
Do not use Django's development server as a production deployment server.

## Automated Testing

Run the complete test suite:

```powershell
python manage.py test
```

Run the Django system check:

```powershell
python manage.py check
```

Check whitespace errors in Git changes:

```powershell
git diff --check
```

Recorded test and system-check evidence is available in the `evidence/`
directory. Test results can vary with code and environment changes; rerun
the commands to verify the current checkout.

## Application Routes

| Route | Purpose |
|---|---|
| `/admin/` | Django administration |
| `/employees/` | Employee HTML pages |
| `/departments/` | Department HTML pages |
| `/api/employees/` | List and create employees |
| `/api/employees/<id>/` | Retrieve, update and delete an employee |
| `/api/employees/<id>/deactivate/` | Deactivate an employee |

The employee API supports search, active-status filtering and pagination.
Refer to `docs/api-design.md` for request examples, permissions, validation
rules and response details.

## Documentation

- `docs/requirements.md` — HRMS requirements
- `docs/system-design.md` — system design
- `docs/architecture.md` — architecture overview
- `docs/django-architecture.md` — Django architecture
- `docs/api-design.md` — API contracts and behavior
- `docs/api-flow.md` — request flow
- `docs/database-design.md` — database design
- `docs/hrms-er-diagram.md` — entity relationships

## Security Notes

- Keep `DJANGO_SECRET_KEY` and `HRMS_DB_PASSWORD` private.
- Do not commit `.env` files, passwords, production data or access tokens.
- Use test data for automated testing and demonstrations.
- Review authentication, role permissions and deployment settings before
  exposing the application outside a trusted development environment.

## Current Scope and Known Limitations

- The implemented REST API currently focuses on employee management.
- The department route provides HTML pages; a separate department REST API
  is not currently registered in the main URL configuration.
- Other HRMS modules described in the requirements or design documents
  should not be considered implemented unless supported by application code
  and tests.
- Production deployment, monitoring, backup and recovery procedures require
  environment-specific configuration.

## Git Validation

Check the current branch and working tree:

```powershell
git status
git log -5 --oneline
```
