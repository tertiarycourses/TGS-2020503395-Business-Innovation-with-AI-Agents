# Lab 2: Compare Prompt, Context and Harness Controls

**Duration:** 35 minutes  
**Topic:** 1  

## Objective

Turn an ambiguous request into a measurable task contract and a minimal context package for an agent.

## Deliverable

A prompt-context comparison, AGENTS.md context file, acceptance rubric and a redacted test transcript.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- Lab 1 completed or the trainer demonstration environment.

## Procedure

### Step 1: Read scenario.md and highlight the business outcome, prohibited actions and missing evidence.

### Step 2: Run the ambiguous prompt once in a fresh session and record why the result cannot be accepted.

```bash
hermes
```

### Step 3: Complete task-contract.md with outcome, inputs, authority, acceptance evidence, stop conditions and rollback.

### Step 4: Edit AGENTS.md so the agent receives the fictional organisation rules at session start.

### Step 5: Start a fresh session in this folder and give the improved task contract.

```bash
hermes
```

### Step 6: Compare the two outputs using acceptance-rubric.md; do not reward verbosity.

### Step 7: Remove any sensitive or credential-like content from the transcript and save only the evidence needed for review.

### Step 8: Run the verifier and explain which improvement came from prompting and which came from context engineering.

```bash
python3 verify.py
```

## Acceptance test

The improved run names its evidence, respects the no-send rule and passes every acceptance item; the learner distinguishes prompt wording from context and runtime authority.

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
