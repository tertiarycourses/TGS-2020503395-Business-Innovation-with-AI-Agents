# Lab 7 - Dataverse Plug-ins, Pipeline Stages, Images, Organization Service, and Custom APIs

## Objective

Design and develop Dataverse plug-ins, choose pipeline stages, use execution context, pre/post images, Organization service operations, and custom APIs.

## Scenario

Contoso needs server-side validation: high-priority service requests must create an escalation record and block invalid status changes.

## Tasks

### Step 1 - Choose pipeline stage

Create a table:

| Requirement | Stage | Reason |
|-------------|-------|--------|

Include pre-validation, pre-operation, and post-operation examples.

### Step 2 - Design plug-in logic

Write pseudocode:

```csharp
public void Execute(IServiceProvider serviceProvider)
{
    // Get context, tracing, and organization service.
    // Validate target entity.
    // Use pre/post image where needed.
    // Throw InvalidPluginExecutionException for invalid changes.
}
```

### Step 3 - Plan images

Create an image table:

| Image | Stage | Columns | Purpose |
|-------|-------|---------|---------|

### Step 4 - Register plug-in

Document Plug-in Registration Tool settings:

- Assembly
- Step message
- Primary entity
- Stage
- Mode
- Filtering attributes
- Images

### Step 5 - Design custom API

Define:

- Custom API name
- Request parameters
- Response properties
- Bound or unbound choice
- Plug-in handler
- Security requirement

## Deliverable

Submit pipeline stage table, plug-in pseudocode, image plan, registration notes, and custom API design.

## Checkpoint questions

1. Why are plug-ins useful for server-side enforcement?
2. What is the purpose of pre and post images?
3. When should a custom API be used?

