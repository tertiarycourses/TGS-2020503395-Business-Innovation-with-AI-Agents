# Learner Guide - Microsoft Power Platform Developer (PL-400)

## Course information

- **Course code:** TGS-2023039340
- **Course title:** Microsoft Power Platform Developer (PL-400)
- **Registration:** https://www.tertiarycourses.com.sg/wsq-microsoft-power-platform-developer-pl-400.html
- **Exam reference:** https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400

## Course goal

This learner guide helps you practise the work of a Microsoft Power Platform developer. You will design solution components, extend Dataverse and Power Apps, automate solution deployment, integrate with APIs and Azure services, and troubleshoot developer scenarios using Microsoft Power Platform tools.

## Learning outcomes

By the end of the labs, you should be able to:

1. Analyze requirements and choose between out-of-the-box features, Power Fx, Power Automate, client scripting, plug-ins, custom APIs, connectors, and Azure Functions.
2. Design authentication, authorization, security roles, teams, DLP impact, and least-privilege access for Power Platform solutions.
3. Configure development environments, solutions, dependencies, environment variables, solution layers, and ALM practices.
4. Use Power Platform CLI, pipelines, and build tools in a developer workflow.
5. Implement advanced canvas app Power Fx, reusable component libraries, cloud flow integration, delegation-aware formulas, and app performance improvements.
6. Extend model-driven apps with JavaScript, Client API events, commands, custom pages, and Dataverse Web API calls.
7. Create and package Power Apps Component Framework code components.
8. Develop Dataverse plug-ins, use pipeline stages, execution context, pre/post images, Organization service operations, custom APIs, and business events.
9. Build custom connectors, OpenAPI definitions, connector authentication, policies, Azure Functions, cloud flows, Key Vault, and retry logic.
10. Publish and consume Dataverse events, register service endpoints, synchronize data with change tracking, alternate keys, and UpsertRequest patterns.

## Suggested schedule

### Day 1 - Design, ALM, apps, and user experience

| Time | Activity |
|------|----------|
| 09:00 - 09:30 | Course briefing, PL-400 role expectations, Contoso case study |
| 09:30 - 10:45 | Lab 1 - Technical architecture, security, components, and business logic placement |
| 10:45 - 11:00 | Break |
| 11:00 - 12:15 | Lab 2 - Dataverse security, solutions, environment variables, and ALM |
| 12:15 - 13:15 | Lunch |
| 13:15 - 14:30 | Lab 3 - CLI, pipelines, build tools, and solution layers |
| 14:30 - 14:45 | Break |
| 14:45 - 16:00 | Lab 4 - Canvas apps, Power Fx, components, flows, and performance |
| 16:00 - 17:00 | Lab 5 - Model-driven app client scripting, commands, Web API, and navigation |

### Day 2 - Platform extension, connectors, APIs, integration, and readiness

| Time | Activity |
|------|----------|
| 09:00 - 10:15 | Lab 6 - PCF code component |
| 10:15 - 10:30 | Break |
| 10:30 - 11:45 | Lab 7 - Dataverse plug-ins and custom APIs |
| 11:45 - 12:45 | Lunch |
| 12:45 - 14:00 | Lab 8 - Custom connectors, OpenAPI, authentication, policies, and Azure Functions |
| 14:00 - 15:15 | Lab 9 - Platform APIs, cloud flows, Key Vault, and retry logic |
| 15:15 - 15:30 | Break |
| 15:30 - 16:45 | Lab 10 - Dataverse events, synchronization, alternate keys, and readiness |
| 16:45 - 17:00 | Exam readiness review and next steps |

## Case study used throughout the labs

You are a Power Platform developer for **Contoso Service Hub**, a company building a service management solution on Dataverse and Power Apps.

The solution must:

- Store accounts, assets, service requests, approvals, and technician notes in Dataverse.
- Provide a model-driven app for service managers.
- Provide a canvas app for field technicians.
- Use reusable app components.
- Add business logic that validates service requests.
- Integrate with external warranty and inventory APIs.
- Publish events when high-priority requests are created.
- Synchronize data with an external system using alternate keys.
- Use ALM so development, test, and production remain controlled.

## Lab deliverables

Each lab produces a developer artifact:

- Technical design worksheet
- Security and ALM checklist
- CLI command notes
- Power Fx and flow design
- JavaScript client script outline
- PCF component plan
- Plug-in and custom API design
- Custom connector design
- API and cloud flow integration plan
- Event and synchronization design

## Recommended learner folder

Create a folder on your device:

```text
PL-400-Learner-Work/
  design/
  code/
  screenshots/
  commands/
  lab-01-architecture.md
  lab-02-alm.md
  lab-03-cli-pipelines.md
  lab-04-canvas.md
  lab-05-client-scripting.md
  lab-06-pcf.md
  lab-07-plugins.md
  lab-08-connectors-functions.md
  lab-09-apis-flows.md
  lab-10-events-sync-readiness.md
```

## How to complete each lab

1. Read the scenario and objective.
2. Open the listed Microsoft references.
3. Use the maker portal, Power Platform CLI, Visual Studio Code, Visual Studio, or Azure tools as required.
4. If tenant access is unavailable, complete the design worksheet and code skeleton sections.
5. Record assumptions and implementation decisions.
6. Answer checkpoint questions.
7. Save code snippets, command logs, and screenshots before moving on.

## Exam preparation guidance

When preparing for PL-400, focus on:

- Matching requirements to the right Power Platform extension point.
- Understanding Dataverse security and solution lifecycle.
- Using developer tooling in repeatable workflows.
- Knowing when to use client-side logic, server-side plug-ins, custom APIs, flows, connectors, or Azure Functions.
- Implementing authentication, retry, error handling, performance, and governance patterns.
- Explaining integration and synchronization patterns clearly.

## Final capstone expectation

At the end of Lab 10, you should have a complete developer solution plan that includes:

- Technical architecture and component design
- Security and ALM model
- App improvement plan
- Client scripting and PCF extension plan
- Plug-in and custom API plan
- Connector, Azure Function, and cloud flow plan
- Event and synchronization plan
- PL-400 readiness tracker

