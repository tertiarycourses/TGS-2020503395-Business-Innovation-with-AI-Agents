# Lab 5 - Model-Driven App Client Scripting, Commands, Web API, and Navigation

## Objective

Extend model-driven apps with JavaScript client scripting, event handlers, commands, buttons, Dataverse Web API calls, and navigation to custom pages.

## Scenario

Service managers use a model-driven app. They need automatic field validation, a command to escalate requests, and navigation to a custom page.

## Tasks

### Step 1 - Choose client scripting events

Create an event table:

| Requirement | Event | Function |
|-------------|-------|----------|

Include form onload, field onchange, and save validation.

### Step 2 - Write Client API pseudocode

Document JavaScript logic:

```javascript
function onPriorityChange(executionContext) {
  const formContext = executionContext.getFormContext();
  const priority = formContext.getAttribute("contoso_priority").getValue();
  if (priority === 1) {
    formContext.ui.setFormNotification("High priority requires manager review.", "WARNING", "priority_warning");
  }
}
```

### Step 3 - Register event handlers

Document:

- Web resource name
- Form library
- Event
- Function name
- Pass execution context setting

### Step 4 - Design command behavior

Create a command plan:

| Command | Visibility rule | Action |
|---------|-----------------|--------|

Include a Power Fx command and a JavaScript command.

### Step 5 - Plan Web API and navigation

Describe how to:

- Retrieve related asset data.
- Update escalation flag.
- Navigate to a custom page.
- Handle errors.

## Deliverable

Submit event table, JavaScript snippet, handler registration notes, command plan, and Web API/navigation design.

## Checkpoint questions

1. Why should execution context be passed?
2. When is client scripting appropriate?
3. What is the risk of putting secure business rules only in JavaScript?

