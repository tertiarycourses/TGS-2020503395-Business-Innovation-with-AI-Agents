# Lab 1: Install Hermes Agent and Run a Safe First Session

**Duration:** 35 minutes  
**Topic:** 3  

## Objective

Install Hermes through the official path, complete provider setup, verify the runtime and run a bounded read-only task.

## Deliverable

An installation verification record with version, doctor result, provider route, session evidence and cleanup status.

## Prerequisites

- A trainer-approved laptop and classroom workspace.
- Use only fictional data supplied in this lab.
- Do not paste API keys, customer data or personal information into evidence.
- A provider account or trainer-provided classroom route; never submit its credential.

## Procedure

### Step 1: Open the official Hermes repository and verify the publisher is NousResearch and the connection uses HTTPS.

### Step 2: Review the installer before execution if required by organisational policy. On macOS, Linux or WSL2, run the official installer.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

### Step 3: Reload the shell so the hermes command is on PATH.

```bash
source ~/.zshrc  # macOS zsh
# or: source ~/.bashrc
```

### Step 4: Start the setup wizard. Select the trainer-approved provider and store credentials only in the Hermes-managed location.

```bash
hermes setup
```

### Step 5: Record version and diagnostics without recording secret values.

```bash
hermes --version
hermes doctor
hermes config check
```

### Step 6: Start Hermes in the lab folder and ask it to summarise the fictional business brief without changing files.

```bash
hermes
```

### Step 7: Confirm the response cites the supplied brief, states uncertainty and makes no external action.

### Step 8: Complete installation-verification.md and run the bundle verifier.

```bash
python3 verify.py
```

### Step 9: Exit the session. If a classroom credential was temporary, revoke it with the trainer.

## Acceptance test

Hermes starts, diagnostics identify a configured provider, the first response uses only fictional evidence, and installation-verification.md is complete.

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
