# Lab 9 - Dataverse Web API, Organization Service, Cloud Flows, Key Vault, and Retry Logic

## Objective

Use platform APIs and Power Automate flows with authentication, retry policies, sensitive input/output handling, Azure Key Vault, and reusable child flows.

## Scenario

Contoso integrations need to create records, update request status, handle transient errors, and protect secrets used by HTTP actions.

## Tasks

### Step 1 - Compare API options

Create a table:

| API or service | Best for | Notes |
|----------------|----------|-------|
| Dataverse Web API | | |
| Organization service | | |
| Custom API | | |
| Power Automate Dataverse connector | | |

### Step 2 - Design Web API operations

Document:

- Create service request.
- Retrieve customer assets.
- Update escalation status.
- Query with filters.
- Handle pagination.

### Step 3 - Plan retry and throttling behavior

Define:

- API limit handling
- Retry policy
- Exponential backoff
- Idempotency
- Bulk operation strategy

### Step 4 - Configure cloud flow design

Create a flow plan:

| Step | Action | Error handling |
|------|--------|----------------|

Include Dataverse trigger, conditions, scopes, run after, child flow, and notification.

### Step 5 - Protect sensitive values

Document:

- Secure inputs and outputs
- Azure Key Vault usage
- Environment variables
- Service principal use
- Secret rotation

## Deliverable

Submit API comparison, Web API operation plan, retry/throttling design, cloud flow plan, and secret protection checklist.

## Checkpoint questions

1. Why should integrations handle retries?
2. What does idempotency mean in synchronization?
3. Why should sensitive flow inputs and outputs be secured?

