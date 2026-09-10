# Lab 5: Orchestrate Specialist Subagents

**Duration:** 45 minutes  
**Topic:** 4  

## Objective

Split one campaign problem into isolated research, audience and risk tasks with structured evidence handoffs.

## Deliverable

A task graph, three specialist handoffs, conflict-resolution note and human decision record.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- Lab 4 skill and memory distinction.

## Procedure

### Step 1: Read campaign-brief.md and define three independent specialist outputs.

### Step 2: Complete task-graph.md with parents, dependencies, acceptance criteria and stop conditions.

### Step 3: Use delegate_task in Hermes or the trainer demonstration to run research, audience and risk specialists in isolated contexts.

```bash
hermes chat --toolsets file,web,delegation
```

### Step 4: Require every specialist to return the handoff schema in handoff-template.md.

### Step 5: Do not give specialists publication, messaging or spending tools.

### Step 6: Compare handoffs. If claims conflict, keep both evidence trails and route them to the reviewer.

### Step 7: Synthesize only after all parent tasks are complete; record missing evidence as a blocker.

### Step 8: Complete human-decision.md and run the verifier.

```bash
python3 verify.py
```

## Acceptance test

Three role-bounded handoffs exist, conflicts remain visible, the synthesis waits for dependencies and the human decision record controls release.

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
