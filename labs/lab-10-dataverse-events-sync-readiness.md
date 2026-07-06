# Lab 10 - Dataverse Events, Service Endpoints, Synchronization, Alternate Keys, and Exam Readiness

## Objective

Publish and consume Dataverse events, register service endpoints, design data synchronization with change tracking, alternate keys, UpsertRequest, and complete PL-400 readiness review.

## Scenario

Contoso must publish high-priority service request events to integration services and synchronize warranty records with an external system.

## Tasks

### Step 1 - Design event publishing

Create an event table:

| Event | Trigger | Subscriber | Payload |
|-------|---------|------------|---------|

Include service request created, request escalated, and request resolved.

### Step 2 - Choose service endpoint

Compare:

| Endpoint | Best for | Notes |
|----------|----------|-------|
| Webhook | | |
| Azure Service Bus | | |
| Azure Event Hub | | |

### Step 3 - Register service endpoint plan

Document:

- Endpoint type
- Authentication
- Message
- Entity
- Filtering attributes
- Retry behavior
- Monitoring

### Step 4 - Design synchronization

Define:

- External key
- Dataverse alternate key
- Change tracking scope
- Upsert strategy
- Conflict handling
- Error logging

### Step 5 - Build exam readiness tracker

Create a table:

| PL-400 area | Confidence 1-5 | Evidence from labs | Next study action |
|-------------|----------------|--------------------|-------------------|

Use the six current PL-400 skill areas:

- Create a technical design
- Build Power Platform solutions
- Implement Power Apps improvements
- Extend the user experience
- Extend the platform
- Develop integrations

## Deliverable

Submit event design, endpoint comparison, service endpoint registration plan, synchronization design, and PL-400 readiness tracker.

## Checkpoint questions

1. When should Azure Service Bus be preferred over a webhook?
2. Why are alternate keys useful for synchronization?
3. Which PL-400 domain needs your most review?

