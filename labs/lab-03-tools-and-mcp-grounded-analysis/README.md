# Lab 3: Demonstrate Tools and an MCP Design Boundary

**Duration:** 40 minutes  
**Topic:** 3  

## Objective

Use file and terminal tools for a grounded calculation, then design a least-privilege MCP connection without live credentials.

## Deliverable

A calculated service analysis, tool trace, MCP trust register and failure record.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- Lab 2 task-contract pattern.

## Procedure

### Step 1: Inspect mock-tickets.csv and data-dictionary.md. Confirm the data is fictional.

### Step 2: Ask Hermes to calculate ticket count, median resolution time and breach rate using a terminal or code-execution tool.

```bash
hermes chat --toolsets file,terminal
```

### Step 3: Require the agent to save analysis.md and include the calculation method.

### Step 4: Run independent-check.py and compare its result with the agent output.

```bash
python3 independent-check.py
```

### Step 5: Complete mcp-design-template.md for a hypothetical CRM server: transport, scopes, read/write tools, trust tier and approval rules.

### Step 6: Mark every write-capable MCP tool as approval-required and exclude customer secrets from prompts and logs.

### Step 7: Record one failed or blocked tool call and identify whether the owning boundary was schema, permission, execution or evidence.

### Step 8: Run the bundle verifier.

```bash
python3 verify.py
```

## Acceptance test

Independent calculations match the reported metrics, every claim points to the mock file, and the MCP design exposes only necessary capabilities.

## Evidence checklist

- [ ] Commands or configuration used (with secrets redacted)
- [ ] Screenshot or generated-file evidence
- [ ] Acceptance test result
- [ ] One failure and how it was resolved
- [ ] Reflection: one control or improvement

## Safety and cleanup

- Use fictional data only.
- Never submit `.env`, tokens, keys or personal information.
- Stop classroom gateways and remove recurring jobs after evidence capture.

## References

- [Official course page](https://www.tertiarycourses.com.sg/wsq-business-innovation-with-ai-agents.html)
- [Hermes Agent repository](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs/)
- [Hermes tools reference](https://hermes-agent.nousresearch.com/docs/reference/tools-reference)
- [Hermes toolsets reference](https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference)
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Hermes memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
- [Hermes context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- [Hermes security](https://hermes-agent.nousresearch.com/docs/user-guide/security)
- [Hermes subagents](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)
- [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Hermes video tools](https://hermes-agent.nousresearch.com/docs/reference/tools-reference#video_gen-toolset)
- Generative AI for Business Innovation — Reference ebook by Brajesh De, 2026
- The Agentic AI Revolution — Reference ebook by Will Hawkins and Nancie Calder, 2025
- Mastering AI Agents — Reference ebook by Marcus Lighthaven, 2025
- Untangling AI — Reference ebook by Matt Kesby, 2026
