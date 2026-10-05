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