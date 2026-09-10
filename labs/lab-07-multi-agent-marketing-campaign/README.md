# Lab 7: Create a Marketing Campaign with Multiple AI Agents

**Duration:** 55 minutes  
**Topic:** 4  

## Objective

Coordinate research, audience, strategy, copy and review agents to produce a source-backed campaign pack that stops before publication.

## Deliverable

A campaign brief, evidence map, three channel variants, claim review, experiment plan and human approval record.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- Lab 5 structured handoff pattern and Lab 6 business-case model.

## Procedure

### Step 1: Read product-evidence.md, brand-rules.md and audience-data.csv. Treat all facts as fictional classroom data.

### Step 2: Create a coordinator task that assigns research, audience, proposition, creative and risk-review roles.

```bash
hermes chat --toolsets file,web,delegation,skills
```

### Step 3: Give each specialist only the files it needs and the handoff schema in campaign-handoff.md.

### Step 4: Require the research agent to map every factual claim to a supplied source line or label it assumption.

### Step 5: Require the audience agent to define inclusion and exclusion without sensitive inference.

### Step 6: Require the strategy agent to propose one measurable hypothesis and the creative agent to draft email, social and landing-page variants.

### Step 7: Route all variants to the risk reviewer for claim, rights, privacy and brand checks.

### Step 8: Assemble campaign-pack.md only after every handoff has passed or has an explicit blocker.

### Step 9: Complete approval-record.md. Do not send, publish, buy media or modify a CRM.

### Step 10: Run the verifier and conduct a peer challenge of one claim and one audience assumption.

```bash
python3 verify.py
```

## Acceptance test

The campaign pack contains three differentiated channel drafts, a traceable evidence map, an experiment hypothesis, visible unresolved assumptions and human-controlled release.

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
