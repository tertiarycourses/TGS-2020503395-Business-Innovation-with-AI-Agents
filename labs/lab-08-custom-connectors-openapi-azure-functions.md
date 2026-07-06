# Lab 8 - Custom Connectors, OpenAPI, Authentication, Policies, and Azure Functions

## Objective

Design custom connectors, OpenAPI definitions, connector authentication, policies, Azure Functions, and connector data transformations.

## Scenario

Contoso needs to call an external warranty API from Power Apps and Power Automate. The API requires authentication and returns data that needs to be normalized.

## Tasks

### Step 1 - Define API operations

Create an operation table:

| Operation | Method | Path | Purpose |
|-----------|--------|------|---------|

Include get warranty status, create warranty claim, and get inventory availability.

### Step 2 - Create OpenAPI outline

Document:

- Base URL
- Paths
- Parameters
- Request body
- Responses
- Error schema

### Step 3 - Choose authentication

Compare:

| Authentication | Best for | Risk |
|----------------|----------|------|
| API key | | |
| OAuth 2.0 | | |
| Azure AD / Microsoft Entra ID | | |

### Step 4 - Configure connector policies

Plan policies to:

- Set header value.
- Rewrite URL.
- Limit response fields.
- Transform response body.
- Add tracking ID.

### Step 5 - Design Azure Function wrapper

Define:

- Trigger type
- Input parameters
- Managed identity or secret handling
- Error handling
- Return schema
- Logging

## Deliverable

Submit API operation table, OpenAPI outline, authentication comparison, connector policy plan, and Azure Function wrapper design.

## Checkpoint questions

1. Why does a custom connector need an OpenAPI definition?
2. When is OAuth better than an API key?
3. Why might an Azure Function wrap an external API?

