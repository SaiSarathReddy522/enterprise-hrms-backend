\# HRMS System Architecture



\## 1. Purpose



This document describes the architecture of the Enterprise HRMS Backend project. The implemented employee API uses Python, Django, Django REST Framework (DRF), and PostgreSQL.



\## 2. Technology Stack



\- \*\*Python:\*\* Programming language.

\- \*\*Django:\*\* Web framework and application structure.

\- \*\*Django REST Framework:\*\* REST API views, serializers, authentication, and permissions.

\- \*\*PostgreSQL:\*\* Relational database.

\- \*\*Git and GitHub:\*\* Version control and source-code hosting.

\- \*\*Django Test Framework:\*\* Automated tests.



\## 3. Architecture Flow



```text

Client / API Consumer

&#x20;       |

&#x20;       v

Django URL Routing

&#x20;       |

&#x20;       v

DRF API View

&#x20;       |

&#x20;       v

Authentication

&#x20;       |

&#x20;       v

Employee Role Permissions

&#x20;       |

&#x20;       v

Serializer Validation

&#x20;       |

&#x20;       v

Employee Service / ORM

&#x20;       |

&#x20;       v

PostgreSQL Database

&#x20;       |

&#x20;       v

Serialized HTTP Response

```



The diagram represents the general request flow. The exact execution order depends on the endpoint and the configured DRF lifecycle.



\## 4. Main Components



\### URL Routing



Routes requests to the appropriate view. The employee REST API includes list, detail, and deactivate endpoints.



\### API Views



Handle HTTP requests, invoke application logic, and return HTTP responses.



\### Authentication and Permissions



Authentication identifies the requesting user. Permission checks determine whether that user may perform the requested operation.



The project includes employee role permissions for Admin, HR, Manager, and Employee groups. Access depends on the configured permission rules and the request type.



\### Serializers



Validate incoming data and convert employee model instances into API response data. Department details are included through the employee serializer.



\### Service Layer



Contains reusable employee operations, including creation, updating, searching, and deactivation.



\### Models and ORM



Django models define the database entities and relationships. The ORM translates supported database operations into SQL.



\### PostgreSQL



Stores persistent HRMS data, including employee and department records.



\## 5. Database Relationships



\- An employee belongs to a department through a foreign-key relationship.

\- The employee's department relationship uses `PROTECT` to prevent deletion of a department that is still referenced by employees.

\- Employee codes and email addresses are unique according to the model configuration.



Refer to `database-design.md` and `hrms-er-diagram.md` for additional database details.



\## 6. Security Controls



\- Secret key and database password are supplied through environment variables.

\- DRF requires authenticated users by default.

\- Employee role permissions restrict operations according to the configured groups and object-level rules.

\- Serializer and model validation help protect data integrity.

\- Automated tests verify configured permission and API behavior.



Never commit actual credentials, production secrets, or sensitive employee information.



\## 7. Implemented Scope and Limitations



\- The current REST API scope is the employee API.

\- Department information is available through the employee serializer; a standalone Department REST API is not currently documented as implemented.

\- HTML pages and REST API endpoints are separate application interfaces.

\- This architecture describes the current implementation, not a fully deployed production system.

\- Production deployment, monitoring, backups, and external integrations require separate implementation and verification.



\## 8. Validation



Run the following commands from the project root with the virtual environment activated and required environment variables configured:



```powershell

python manage.py check

python manage.py test --keepdb

git diff --check

```



Record the actual command output in the project's evidence files after each relevant validation run.
