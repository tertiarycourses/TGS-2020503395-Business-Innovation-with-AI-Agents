# Lab 3 - Power Platform CLI, Pipelines, Build Tools, and Solution Layers

## Objective

Use or document Power Platform CLI, pipelines, build tools, CI/CD automation, and solution layer troubleshooting.

## Scenario

Contoso wants repeatable deployment. Developers need to unpack solutions, store source in Git, validate changes, and promote releases through environments.

## Tasks

### Step 1 - Install and authenticate CLI

Document commands:

```powershell
pac auth create --url https://yourorg.crm.dynamics.com
pac org who
```

### Step 2 - Export and unpack a solution

Document:

```powershell
pac solution export --name ContosoServiceHub --path ContosoServiceHub.zip --managed false
pac solution unpack --zipfile ContosoServiceHub.zip --folder src/ContosoServiceHub
```

### Step 3 - Plan source control structure

Create a folder structure:

```text
src/
  solutions/
  plugins/
  pcf/
  connectors/
  flows/
docs/
```

### Step 4 - Design pipeline stages

Create a pipeline:

| Stage | Action | Validation |
|-------|--------|------------|

Include export, unpack, build, static checks, pack, import to test, and deploy to production.

### Step 5 - Troubleshoot solution layers

Create a troubleshooting checklist:

- Identify unmanaged layer.
- Review active layer.
- Check component dependencies.
- Compare version numbers.
- Remove unintended customization.

## Deliverable

Submit CLI command notes, folder structure, pipeline stage table, and solution layer checklist.

## Checkpoint questions

1. Why unpack solutions into source control?
2. What does a managed solution protect?
3. Why are solution layers important during troubleshooting?

