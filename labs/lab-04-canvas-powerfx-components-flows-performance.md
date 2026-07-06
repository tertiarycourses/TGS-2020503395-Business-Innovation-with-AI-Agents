# Lab 4 - Advanced Canvas Apps, Power Fx, Components, Flows, and Performance

## Objective

Implement or design advanced canvas app features using Power Fx, reusable components, cloud flows, Monitor, delegation-aware formulas, and performance optimization.

## Scenario

Technicians use a canvas app to update service requests. The app is slow, formulas are repeated, and some filters do not delegate.

## Tasks

### Step 1 - Design screen and data requirements

Create a table:

| Screen | Data source | User action |
|--------|-------------|-------------|

Include request list, request detail, update status, and photo/note capture.

### Step 2 - Write Power Fx patterns

Document formulas for:

- Filtering open requests
- Patching a status update
- Validating required fields
- Setting global variables
- Handling errors with `IfError`

### Step 3 - Design reusable components

Plan components:

- Header component
- Status badge component
- Request card component
- Confirmation dialog component

### Step 4 - Integrate a cloud flow

Design a button action that calls a cloud flow to:

1. Validate request status.
2. Notify manager.
3. Write audit details.
4. Return result to app.

### Step 5 - Optimize performance

Checklist:

- Reduce controls per screen.
- Preload reference data.
- Avoid non-delegable filters on large data.
- Use Monitor for troubleshooting.
- Cache repeated lookups carefully.

## Deliverable

Submit screen/data table, Power Fx snippets, component plan, cloud flow integration plan, and performance checklist.

## Checkpoint questions

1. Why does delegation matter?
2. When should a reusable component be created?
3. What does Monitor help diagnose?

