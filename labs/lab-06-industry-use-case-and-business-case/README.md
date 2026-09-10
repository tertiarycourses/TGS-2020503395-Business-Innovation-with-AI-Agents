# Lab 6: Prioritise Ten Industry Use Cases

**Duration:** 45 minutes  
**Topic:** 2  

## Objective

Score the ten realistic use cases for value, feasibility, risk and evidence readiness, then calculate a risk-adjusted pilot case.

## Deliverable

A completed opportunity matrix, transparent cost-benefit calculation, pilot charter and stop decision.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- Topic 2 feasibility framework.

## Procedure

### Step 1: Review ten-use-cases.csv and confirm each row has a trigger, output and human gate.

### Step 2: Choose weights for value, feasibility, governability and evidence readiness in scoring-method.md.

### Step 3: Ask Hermes to calculate weighted scores and preserve the formula and input values.

```bash
hermes chat --toolsets file,terminal
```

### Step 4: Challenge the top-ranked case with a failure-loss and review-cost estimate.

### Step 5: Complete cost-benefit.csv for a 12-week pilot using scenario assumptions.

### Step 6: Calculate net benefit, benefit-cost ratio and break-even volume; label all assumptions.

```bash
python3 calculate_case.py
```

### Step 7: Define go, revise and stop thresholds in pilot-charter.md.

### Step 8: Run the verifier and defend the selected pilot to a peer reviewer.

```bash
python3 verify.py
```

## Acceptance test

The selected case wins under the documented weights, the arithmetic is reproducible, risks and review cost are included, and the pilot has a measurable stop condition.

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
