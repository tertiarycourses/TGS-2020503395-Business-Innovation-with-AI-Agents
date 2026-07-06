# Lab 6 - Power Apps Component Framework Code Component

## Objective

Design, create, package, deploy, and consume a Power Apps Component Framework code component.

## Scenario

Contoso wants a reusable priority indicator component that can be used in model-driven apps to show request urgency with custom rendering.

## Tasks

### Step 1 - Define component requirements

Create a component specification:

| Property | Type | Purpose |
|----------|------|---------|

Include priority value, label, color, and read-only state.

### Step 2 - Initialize PCF project

Document commands:

```powershell
pac pcf init --namespace Contoso --name PriorityIndicator --template field
npm install
npm run build
```

### Step 3 - Explain lifecycle methods

Describe:

- `init`
- `updateView`
- `getOutputs`
- `destroy`

### Step 4 - Configure manifest concept

Document:

- Control namespace
- Property definitions
- Dataset or field binding
- Resources
- Feature usage such as Web API or Utility if required

### Step 5 - Package and consume

Document:

1. Create solution project.
2. Add PCF component.
3. Build solution.
4. Import into environment.
5. Add component to form field.
6. Test rendering and behavior.

## Deliverable

Submit component specification, CLI command notes, lifecycle explanation, manifest notes, and package/deploy checklist.

## Checkpoint questions

1. Why are PCF components useful?
2. Which lifecycle method updates the UI?
3. Why should component dependencies be included in a solution?

