# HRMS Recovery and Troubleshooting Runbook

## 1. Purpose

This runbook explains how to diagnose common development and testing
failures in the Enterprise HRMS Backend.

## 2. Safety Rules

- Use development or test data only.
- Never put passwords, secret keys, tokens or personal employee data
  in logs, screenshots or Git commits.
- Do not delete the PostgreSQL database to troubleshoot a failure.
- Do not run destructive database commands without an approved backup
  and confirmation that the target is not a production database.

## 3. Required Environment Variables

The application expects:

- `DJANGO_SECRET_KEY`
- `HRMS_DB_PASSWORD`

Check whether each variable is present without displaying its value:

```powershell
if ($env:DJANGO_SECRET_KEY) { "DJANGO_SECRET_KEY is set" } else { "DJANGO_SECRET_KEY is missing" }
if ($env:HRMS_DB_PASSWORD) { "HRMS_DB_PASSWORD is set" } else { "HRMS_DB_PASSWORD is missing" }
```

If a variable is missing, set it again in the current PowerShell session.
Follow the setup instructions in `README.md`. These variables may need
to be configured again after opening a new terminal.

## 4. Django Startup or Configuration Failure

Run:

```powershell
python manage.py check
```

If the check fails:

1. Read the first traceback and identify the setting or module named.
2. Confirm the virtual environment is activated.
3. Confirm dependencies are installed using `python -m pip install -r requirements.txt`.
4. Confirm required environment variables are present.
5. Correct the underlying problem and rerun the check.

Do not copy secret values into error reports.

## 5. PostgreSQL Connection Failure

Symptoms may include connection refused, authentication failure or
database does not exist.

1. Confirm the PostgreSQL service is running.
2. Confirm the database host and port in `config/settings.py`.
3. Confirm the configured database and database user exist.
4. Confirm `HRMS_DB_PASSWORD` is set correctly in the current session.
5. Run `python manage.py check` and then `python manage.py migrate`
   after resolving the connection issue.

Do not reset credentials or remove databases as a first troubleshooting step.

## 6. Migration Failure

Run:

```powershell
python manage.py showmigrations
python manage.py migrate
```

If a migration fails:

1. Read the complete error locally.
2. Check database connectivity and migration dependencies.
3. Review recent model and migration changes.
4. Preserve the database and collect the error details without secrets.
5. Resolve the cause before retrying.

Do not edit already-applied migrations or delete migration history as
a quick fix.

## 7. Automated Test Failure

Run:

```powershell
python manage.py test
```

If a test fails:

1. Record the failing test name and assertion.
2. Check whether the failure is caused by code, settings or test data.
3. Confirm tests use isolated test data.
4. Fix the cause and rerun the failing test or relevant test class.
5. Rerun the complete suite before committing.

Capture only sanitized output in evidence files.

## 8. Database Error Responses

The employee API includes tests for database integrity failures and
employee-list database failures. Use the automated tests to verify
these behaviors after relevant code changes.

Do not intentionally interrupt or damage a shared database to reproduce
a failure. Use isolated test data or a safe test environment.

## 9. Git Recovery

Inspect the current state before changing anything:

```powershell
git status
git diff --check
git diff
```

If a change is unexpected, inspect it before staging or committing.
Avoid `git reset --hard`, deleting files or force-pushing as routine
recovery steps.

If a commit has already been pushed, coordinate with the project owner
before rewriting shared history.

## 10. Post-Recovery Verification

After fixing a problem, run:

```powershell
python manage.py check
python manage.py test
git diff --check
git status
```

Review all changes, ensure no secrets or sensitive data are included,
and commit only the intended files.

## 11. Known Limitations

- The current REST API focuses on employee management.
- A separate department REST API is not registered in the main URL configuration.
- Production backup, restore, monitoring and deployment procedures
  require environment-specific implementation and validation.
- A successful local test run does not by itself prove production readiness.
