# Lab 1 - Technical Architecture, Security, Components, and Business Logic Placement

## Objective

Create a technical design that identifies solution components, security impact, business logic placement, and extension approach.

## Scenario

Contoso Service Hub needs a service request solution with Dataverse tables, model-driven forms, a technician canvas app, validation logic, API integration, and ALM.

## Tasks

### Step 1 - Identify solution components

Create a table:

| Requirement | Component | Build approach |
|-------------|-----------|----------------|

Include Dataverse tables, model-driven app, canvas app, Power Automate flow, plug-in, custom connector, Azure Function, and report.

### Step 2 - Decide business logic placement

Compare:

| Logic | Best location | Reason |
|-------|---------------|--------|

Include business rules, Power Fx, cloud flows, client script, plug-ins, and Azure Functions.

### Step 3 - Design authentication and authorization

Document:

- User roles
- Security roles
- Teams and business units
- Row sharing rules
- External API authentication
- Service principal use

### Step 4 - Choose table and integration patterns

Decide where to use:

- Standard tables
- Custom Dataverse tables
- Virtual tables
- Elastic tables
- Connectors

### Step 5 - Assess DLP and security constraints

Create a risk table:

| Constraint | Impact | Mitigation |
|------------|--------|------------|

Include DLP policies, least privilege, environment boundaries, and connector classification.

## Deliverable

Submit a technical design worksheet with components, business logic placement, authentication/authorization, table choices, and security constraints.

## Checkpoint questions

1. When should logic be implemented server-side instead of client-side?
2. Why should connector choice be reviewed against DLP policies?
3. What is the risk of overusing custom code?

