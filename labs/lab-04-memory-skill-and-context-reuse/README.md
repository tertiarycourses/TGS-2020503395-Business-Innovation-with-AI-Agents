# Lab 4: Demonstrate Memory Skills and Context Reuse

**Duration:** 40 minutes  
**Topic:** 3  

## Objective

Separate durable business memory from reusable procedural skills and verify both on a new fictional case.

## Deliverable

A memory decision log, a review-ready campaign skill, a second-case test and a correction record.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- Labs 2 and 3 completed.

## Procedure

### Step 1: Read memory-candidates.md. Classify each item as durable memory, task context, skill instruction or prohibited secret.

### Step 2: Save only the approved durable fictional preferences using Hermes memory; never save the token-shaped marker.

```bash
hermes chat --toolsets memory,skills,file
```

### Step 3: Create or revise a local skill from skill-template.md for evidence-led campaign briefing.

### Step 4: Inspect the skill trigger, scope, method, verification and stop conditions.

### Step 5: Start a fresh session with new-case.md and load the skill.

```bash
hermes
```

### Step 6: Verify the new output uses durable preferences but does not copy transient facts from the first case.

### Step 7: Correct one fictional preference, rerun the test and record the before/after behaviour.

### Step 8: Complete memory-decision-log.md and run the verifier.

```bash
python3 verify.py
```

## Acceptance test

The second case demonstrates durable preference reuse, procedural skill reuse, correction and zero secret or transient-noise retention.

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
