# Lab 8: Create a Governed Multi-Agent Video Campaign

**Duration:** 55 minutes  
**Topic:** 5  

## Objective

Produce a review-ready video campaign package with specialist agents, rights and consent controls, security tests and a human release gate.

## Deliverable

A script, storyboard, asset and rights register, generation plan, QC report, security matrix and final human release decision.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- Lab 7 approved campaign evidence; trainer-approved media tools if generation is demonstrated.

## Procedure

### Step 1: Read approved-campaign-input.md. Confirm no real person, customer, copyrighted music or external publication destination is authorised.

### Step 2: Delegate script, storyboard, asset, factual-review and accessibility tasks with isolated context packages.

```bash
hermes chat --toolsets file,delegation,skills
```

### Step 3: Require the script agent to use only approved product claims and include a clear call to action without deceptive urgency.

### Step 4: Require the storyboard agent to define six scenes with framing, action, duration and continuity notes.

### Step 5: Complete asset-rights-register.csv for every generated or supplied asset, including prompt, owner, licence, consent and allowed use.

### Step 6: If a trainer-approved video tool is available, create an internal low-resolution preview only. Otherwise complete generation-plan.md without calling an external service.

```bash
hermes chat --toolsets file,delegation,video_gen
```

### Step 7: Run factual, visual, audio, caption and brand QC; record failures and required revisions in qc-report.md.

### Step 8: Complete security-boundary-test-matrix.md with negative tests for unapproved data, external send, unsafe URL, secret-like marker and unauthorised likeness.

### Step 9: Apply the human release checklist. Keep the decision at revise unless every rights, consent, factual and accessibility item passes.

### Step 10: Remove temporary media and credentials, run the verifier and retain only redacted evidence.

```bash
python3 verify.py
```

## Acceptance test

The production package is complete and traceable, no unapproved asset or claim is used, negative controls block unsafe actions, and only a named human can approve final release.

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
