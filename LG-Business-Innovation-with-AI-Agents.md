# Business Innovation with AI Agents — Learner Guide

**Course code:** TGS-2020503395  
**Version:** v23.0 · 11 September 2026

## Learning Outcomes

- LO1: Compare the 2023 prompt, 2024 context, 2025 harness and 2026 agent engineering paradigms and evaluate their impact on business models.
- LO2: Identify and prioritise realistic AI-agent opportunities using process evidence, value measures and human accountability.
- LO3: Digitalise a bounded workflow with Hermes Agent tools, context, memory, skills and specialist subagents.
- LO4: Conduct feasibility and cost-benefit analysis for an AI-agent pilot using measurable assumptions and risk-adjusted controls.
- LO5: Implement and evaluate a governed multi-agent marketing or video campaign with security, data governance and human release approval.

## Topic 1: AI Engineering Evolution and Agent Architecture

Trace the engineering shift from single responses to governed goal-directed systems and map the human brain-body analogy to model-harness design.

### 2023–2026 engineering timeline

1. 2023 Prompt engineering: shape one response
2. 2024 Context engineering: assemble the right evidence
3. 2025 Harness engineering: control tools and runtime
4. 2026 AI agents: pursue goals through verified loops

### Prompt engineering and context engineering

- **Prompt engineering:** Instruction wording; Examples and output schema; Single-turn optimisation; Failure: underspecified intent
- **Context engineering:** Evidence selection; Memory and retrieval; Tool results and state; Failure: irrelevant or stale context

### Harness engineering and agent engineering

- **Harness engineering:** Tool registry and permissions; Session lifecycle and retries; Observability and approvals; Deterministic runtime controls
- **Agent engineering:** Goal decomposition; Dynamic tool selection; Observation and replanning; Human accountability for impact

### Engineering leverage shifts outward

Business reliability increasingly depends on the system around the model, not only the model response.

### Agent operating loop

1. Interpret goal and authority
2. Plan the next bounded action
3. Use an authorised tool
4. Observe state and evidence
5. Revise, stop or request approval

### Human and AI-agent operating systems

- **Human: brain + body:** Brain reasons from perception and memory; Body senses and acts in the world; Values and accountability remain human; Fatigue and attention constrain execution
- **AI agent: model + harness:** Model predicts and reasons over context; Harness exposes tools, state and controls; No independent moral or legal accountability; Compute and data constrain execution

### The harness has six control planes

- **Context** — Instructions, files, retrieval and current state.
- **Tools** — Typed actions for files, web, APIs and applications.
- **Memory** — Curated facts and past evidence across sessions.
- **Orchestration** — Planning, delegation, scheduling and handoffs.
- **Safety** — Permissions, sandboxing, approvals and policy.
- **Observability** — Logs, traces, tests, cost and outcome metrics.

### What the harness does on each turn

1. Assemble system and project context
2. Expose only permitted tool schemas
3. Execute one action in a bounded backend
4. Persist selected state and telemetry
5. Return evidence to model and operator

### Where agent systems fail

- **Goal** — Ambiguous outcome or no stop condition.
- **Grounding** — Missing, stale or poisoned evidence.
- **Authority** — Tool scope exceeds business need.
- **Verification** — Plausible narrative replaces observed state.

### Autonomy follows consequence

As reversibility falls and external impact rises, explicit human approval should increase.

### Four kinds of agent evidence

- **Input provenance** — Where facts, files and instructions came from.
- **Execution trace** — Which tool ran with which bounded arguments.
- **State proof** — What file, record or status changed.
- **Decision record** — Who approved, rejected or revised the outcome.

### Model plus harness in the workplace

The model proposes; the harness constrains, acts, records and returns control to people.
- Editable labels stay in PowerPoint
- Approval is a system state
- Evidence closes the loop

### Copilot and agent

- **Copilot interaction:** Human initiates each turn; Recommendation is the main output; Tools are often user-triggered; Context usually ends with the session
- **Agent operation:** Goal can span several actions; State changes can be the output; Tools are selected during the loop; Sessions, memory and schedules create continuity

### Safe task contract

1. Name the business outcome
2. Define allowed data and systems
3. Set approval thresholds
4. Specify acceptance evidence
5. Add stop and rollback conditions


## AI-Agent Use-Case Catalog — 10 Workflow Patterns

These are bounded workflow patterns. Begin read-only or draft-only, then add higher-impact capabilities only after the pilot is observable, reliable and approval-gated.

### Customer and Revenue

Draft, analyse and recommend while people retain customer and commercial authority.

#### UC-01: Retail service recovery

- **Trigger:** New complaint with order ID
- **Hermes workflow:** Retrieve order facts, policy and prior contact; propose response and remedy band.
- **Capabilities:** CRM MCP · policy skill · memory
- **Reviewable output:** Grounded reply draft and escalation
- **Human authority:** Agent cannot refund or send without approval
- **Runtime / risk:** Hybrid · Medium
- **Evidence:** Order source, policy citations, approver and final action
- **Source pattern:** Generative AI for Business Innovation; Hermes tools

#### UC-02: B2B lead intelligence

- **Trigger:** Approved target-account list
- **Hermes workflow:** Delegate research, verify sources, score fit and draft outreach angles.
- **Capabilities:** Web · delegation · CRM MCP
- **Reviewable output:** Account brief and draft sequence
- **Human authority:** Sales owner approves contact and claims
- **Runtime / risk:** Hybrid · Medium
- **Evidence:** Source URLs, scoring rationale and approval state
- **Source pattern:** Mastering AI Agents; Hermes delegation

### Operations and Supply

Convert recurring operating signals into exception queues and reviewable decisions.

#### UC-03: Manufacturing exception triage

- **Trigger:** Quality or downtime alert
- **Hermes workflow:** Correlate sensor event, maintenance history and SOP; propose diagnostic sequence.
- **Capabilities:** Files · data MCP · skill
- **Reviewable output:** Prioritised diagnostic brief
- **Human authority:** Engineer authorises any equipment action
- **Runtime / risk:** Local · High
- **Evidence:** Signal IDs, thresholds, SOP version and decision
- **Source pattern:** Generative AI for Business Innovation

#### UC-04: Logistics disruption planner

- **Trigger:** Late shipment or route closure
- **Hermes workflow:** Compare commitments, alternatives, cost and customer impact; propose reroute options.
- **Capabilities:** Web · logistics MCP · calculator
- **Reviewable output:** Option matrix with constraints
- **Human authority:** Operations owner approves reroute and spend
- **Runtime / risk:** Hybrid · High
- **Evidence:** Shipment IDs, rates, assumptions and approval
- **Source pattern:** The Agentic AI Revolution

### Regulated Knowledge Work

Ground high-stakes analysis in approved sources and qualified review.

#### UC-05: Banking KYC review pack

- **Trigger:** Incomplete customer due-diligence file
- **Hermes workflow:** Check required documents, flag inconsistencies and prepare reviewer questions.
- **Capabilities:** Document tools · rules skill · audit log
- **Reviewable output:** Exception pack, not a customer decision
- **Human authority:** Compliance officer makes disposition
- **Runtime / risk:** Controlled · High
- **Evidence:** Document list, rule references and reviewer decision
- **Source pattern:** Generative AI for Business Innovation

#### UC-06: Healthcare discharge education

- **Trigger:** Approved discharge summary
- **Hermes workflow:** Transform clinician-approved instructions into plain-language variants and comprehension questions.
- **Capabilities:** Files · approved knowledge · language skill
- **Reviewable output:** Patient education draft
- **Human authority:** Clinician validates accuracy and suitability
- **Runtime / risk:** Controlled · High
- **Evidence:** Source summary, version, clinical approval and delivery
- **Source pattern:** Generative AI for Business Innovation

### People and Public Service

Improve access and routing without delegating sensitive employment or public decisions.

#### UC-07: HR policy navigator

- **Trigger:** Employee policy question
- **Hermes workflow:** Retrieve current policy clauses, draft an answer and route exceptions.
- **Capabilities:** RAG · files · memory
- **Reviewable output:** Cited answer or escalation
- **Human authority:** HR decides eligibility and exceptions
- **Runtime / risk:** Private · Medium
- **Evidence:** Policy version, citations, confidence and escalation
- **Source pattern:** The Agentic AI Revolution

#### UC-08: Municipal case intake

- **Trigger:** Resident service request
- **Hermes workflow:** Classify issue, verify location evidence, draft routing and identify missing information.
- **Capabilities:** Forms · geodata MCP · workflow
- **Reviewable output:** Structured intake and routing proposal
- **Human authority:** Officer confirms category and priority
- **Runtime / risk:** Controlled · Medium
- **Evidence:** Case ID, data basis and routing decision
- **Source pattern:** Untangling AI

### Marketing and Media

Separate research, creation, review and publication into accountable specialist roles.

#### UC-09: Multi-agent marketing campaign

- **Trigger:** Approved product and audience brief
- **Hermes workflow:** Research, segment, position, draft, challenge claims and assemble channel variants.
- **Capabilities:** Delegation · web · skills · files
- **Reviewable output:** Campaign pack with evidence map
- **Human authority:** Brand owner approves claims, spend and release
- **Runtime / risk:** Hybrid · Medium
- **Evidence:** Sources, claim register, revisions and sign-off
- **Source pattern:** Mastering AI Agents; Hermes delegation

#### UC-10: Multi-agent video campaign

- **Trigger:** Approved campaign concept
- **Hermes workflow:** Create script, storyboard, asset manifest, rights review, generation plan and QA report.
- **Capabilities:** Delegation · image/video tools · files
- **Reviewable output:** Review-ready production package
- **Human authority:** Human approves likeness, rights and final render
- **Runtime / risk:** Hybrid · High
- **Evidence:** Consent, licences, prompts, QC and release record
- **Source pattern:** Generative AI for Business Innovation; Hermes video tools

### Lab 1: Install Hermes Agent and Run a Safe First Session

Install Hermes through the official path, complete provider setup, verify the runtime and run a bounded read-only task.

#### Detailed procedure

1. Open the official Hermes repository and verify the publisher is NousResearch and the connection uses HTTPS.
2. Review the installer before execution if required by organisational policy. On macOS, Linux or WSL2, run the official installer.

   ```bash
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
   ```

3. Reload the shell so the hermes command is on PATH.

   ```bash
   source ~/.zshrc  # macOS zsh
   # or: source ~/.bashrc
   ```

4. Start the setup wizard. Select the trainer-approved provider and store credentials only in the Hermes-managed location.

   ```bash
   hermes setup
   ```

5. Record version and diagnostics without recording secret values.

   ```bash
   hermes --version
   hermes doctor
   hermes config check
   ```

6. Start Hermes in the lab folder and ask it to summarise the fictional business brief without changing files.

   ```bash
   hermes
   ```

7. Confirm the response cites the supplied brief, states uncertainty and makes no external action.
8. Complete installation-verification.md and run the bundle verifier.

   ```bash
   python3 verify.py
   ```

9. Exit the session. If a classroom credential was temporary, revoke it with the trainer.

**Acceptance test:** Hermes starts, diagnostics identify a configured provider, the first response uses only fictional evidence, and installation-verification.md is complete.

### Lab 2: Compare Prompt, Context and Harness Controls

Turn an ambiguous request into a measurable task contract and a minimal context package for an agent.

#### Detailed procedure

1. Read scenario.md and highlight the business outcome, prohibited actions and missing evidence.
2. Run the ambiguous prompt once in a fresh session and record why the result cannot be accepted.

   ```bash
   hermes
   ```

3. Complete task-contract.md with outcome, inputs, authority, acceptance evidence, stop conditions and rollback.
4. Edit AGENTS.md so the agent receives the fictional organisation rules at session start.
5. Start a fresh session in this folder and give the improved task contract.

   ```bash
   hermes
   ```

6. Compare the two outputs using acceptance-rubric.md; do not reward verbosity.
7. Remove any sensitive or credential-like content from the transcript and save only the evidence needed for review.
8. Run the verifier and explain which improvement came from prompting and which came from context engineering.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** The improved run names its evidence, respects the no-send rule and passes every acceptance item; the learner distinguishes prompt wording from context and runtime authority.


## Topic 2: Business Opportunities and Feasibility

Select realistic AI-agent opportunities from process evidence and build a risk-adjusted business case instead of automating attractive anecdotes.

### Opportunity discovery funnel

1. Map process and pain
2. Locate judgement and information work
3. Define measurable outcome
4. Screen risk and data readiness
5. Select bounded pilot

### Agent-worthy task signals

- **Variable inputs** — Cases differ enough to require interpretation.
- **Tool crossing** — Work spans documents, systems or channels.
- **Feedback** — Intermediate results change the next action.
- **Evidence** — The result can be tested against observable criteria.

### Use automation when the path is known

- **Conventional automation:** Stable rules; Structured inputs; Low ambiguity; High repeat volume
- **AI agent:** Changing evidence; Unstructured inputs; Several valid paths; Human review of judgement

### Process evidence sheet

- **Baseline** — Cycle time, volume, cost and error rate.
- **Bottleneck** — Wait, rework, handoff or search delay.
- **Decision** — Who exercises judgement and with what policy.
- **Target** — Specific measurable future-state change.

### Value hypothesis

1. Business event
2. Agent intervention
3. Changed operating metric
4. Financial or strategic effect
5. Measurement window

### Illustrative opportunity portfolio

Prioritisation combines value, feasibility and governability; the tallest business value alone does not win.

### Feasibility has four lenses

- **Data** — Availability, quality, rights and freshness.
- **Technical** — Models, tools, integration and reliability.
- **Operational** — Owners, exceptions, training and support.
- **Governance** — Privacy, security, compliance and accountability.

### Pilot cost model

1. One-time build and integration
2. Recurring model and tool cost
3. Human review and exception handling
4. Security, monitoring and support
5. Change and adoption cost

### Risk-adjusted benefit

A credible business case subtracts review, expected failure loss and recurring operation—not just software fees.

### Expected value fields

- **Benefit** — Hours saved × loaded cost, revenue lift or loss avoided.
- **Probability** — Observed pilot success rate, not optimism.
- **Exposure** — Volume and consequence per decision.
- **Control cost** — Review, monitoring, incident and audit effort.

### Proof of concept and pilot

- **Proof of concept:** Can the mechanism work?; Small synthetic dataset; Technical learning; No business-scale claim
- **Pilot:** Does it create value in context?; Representative bounded cases; Operational and governance evidence; Go, revise or stop decision

### Pilot scorecard

1. Quality and factuality
2. Cycle time and throughput
3. Human-review burden
4. Safety and control exceptions
5. User and business outcome

### Ten-industry use-case test

- **Specific** — Trigger, inputs and output are named.
- **Controllable** — Human gate and tool scope are explicit.
- **Observable** — Evidence shows whether work succeeded.
- **Economic** — Value exceeds build, run and risk cost.

### Scale or stop

- **Scale signals:** Repeatable quality; Positive risk-adjusted value; Low exception burden; Named operating owner
- **Stop or redesign signals:** Unverifiable output; Sensitive data without controls; Review cost erases value; Failures are hard to detect

### Lab 6: Prioritise Ten Industry Use Cases

Score the ten realistic use cases for value, feasibility, risk and evidence readiness, then calculate a risk-adjusted pilot case.

#### Detailed procedure

1. Review ten-use-cases.csv and confirm each row has a trigger, output and human gate.
2. Choose weights for value, feasibility, governability and evidence readiness in scoring-method.md.
3. Ask Hermes to calculate weighted scores and preserve the formula and input values.

   ```bash
   hermes chat --toolsets file,terminal
   ```

4. Challenge the top-ranked case with a failure-loss and review-cost estimate.
5. Complete cost-benefit.csv for a 12-week pilot using scenario assumptions.
6. Calculate net benefit, benefit-cost ratio and break-even volume; label all assumptions.

   ```bash
   python3 calculate_case.py
   ```

7. Define go, revise and stop thresholds in pilot-charter.md.
8. Run the verifier and defend the selected pilot to a peer reviewer.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** The selected case wins under the documented weights, the arithmetic is reproducible, risks and review cost are included, and the pilot has a measurable stop condition.


## Topic 3: Hermes Agent Harness in Practice

Inspect Hermes Agent as a concrete harness and connect each runtime component to a business control, learner lab and observable output.

### Hermes Agent runtime surface

Hermes combines conversation, tool use, memory, skills and delegation inside one open-source harness.
- Model-flexible
- Local state by default
- Toolsets are configurable

### Supported installation path

1. Official installer
2. Setup wizard
3. Provider authentication
4. Doctor and configuration check
5. Bounded first conversation

### Hermes workspace ownership

- **Configuration** — Provider, toolset and profile settings.
- **Sessions** — Conversation and tool traces for retrieval.
- **Memory** — Curated cross-session knowledge.
- **Skills** — Reusable procedural instructions and assets.

### Context and memory

- **Context:** Available now; Project rules and task files; Tool results and session tail; May be compressed as the session grows
- **Memory:** Selected for later; Preferences and durable facts; Curated rather than full transcript; Must avoid secrets and transient noise

### Toolsets are capability boundaries

- **File** — Read, write and patch within allowed roots.
- **Terminal** — Run commands in a selected backend.
- **Web and browser** — Retrieve changing evidence and operate pages.
- **Delegation** — Spawn isolated specialist contexts.

### Tool call lifecycle

1. Model selects typed tool
2. Harness validates schema and policy
3. Approval gate evaluates impact
4. Backend executes or blocks
5. Result returns as evidence

### Built-in tools and MCP

- **Built-in tool:** Ships with Hermes; Known runtime semantics; Platform availability checks; Updated with Hermes
- **MCP tool:** External server boundary; Server-defined schema; OAuth or secret scope; Trust and filtering need review

### A useful skill contract

- **Trigger** — When the procedure should load.
- **Scope** — What the skill may read or change.
- **Method** — Reusable steps, templates and scripts.
- **Verification** — Evidence and stop conditions.

### Skill improvement loop

1. Run a complex task
2. Capture what worked and failed
3. Write or revise the skill
4. Test on a new case
5. Retain only proven guidance

### Memory quality rules

- **Useful** — Durable information that changes future work.
- **Attributable** — Source and date are known.
- **Minimal** — No secret, noise or redundant transcript.
- **Correctable** — Review and update when evidence changes.

### Hermes CLI as an operating cockpit

The CLI exposes conversation, tool evidence, approvals, usage and subagent state in one operational view.
- Interruptible work
- Visible tool results
- Session continuity

### Fixed context consumes the prompt budget

Unused tool schemas and verbose instructions reduce the space available for task evidence.

### Grounded business answer

1. Receive business question
2. Load project context
3. Retrieve approved evidence
4. Use calculation or system tool
5. Return cited answer and uncertainty

### Session resume and fresh session

- **Resume:** Preserves working history; Good for interrupted work; May carry stale assumptions; Higher context cost
- **Fresh session:** Clean task boundary; Good for scheduled or delegated work; Needs explicit context package; Easier evaluation

### Lab 1: Install Hermes Agent and Run a Safe First Session

Install Hermes through the official path, complete provider setup, verify the runtime and run a bounded read-only task.

#### Detailed procedure

1. Open the official Hermes repository and verify the publisher is NousResearch and the connection uses HTTPS.
2. Review the installer before execution if required by organisational policy. On macOS, Linux or WSL2, run the official installer.

   ```bash
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
   ```

3. Reload the shell so the hermes command is on PATH.

   ```bash
   source ~/.zshrc  # macOS zsh
   # or: source ~/.bashrc
   ```

4. Start the setup wizard. Select the trainer-approved provider and store credentials only in the Hermes-managed location.

   ```bash
   hermes setup
   ```

5. Record version and diagnostics without recording secret values.

   ```bash
   hermes --version
   hermes doctor
   hermes config check
   ```

6. Start Hermes in the lab folder and ask it to summarise the fictional business brief without changing files.

   ```bash
   hermes
   ```

7. Confirm the response cites the supplied brief, states uncertainty and makes no external action.
8. Complete installation-verification.md and run the bundle verifier.

   ```bash
   python3 verify.py
   ```

9. Exit the session. If a classroom credential was temporary, revoke it with the trainer.

**Acceptance test:** Hermes starts, diagnostics identify a configured provider, the first response uses only fictional evidence, and installation-verification.md is complete.

### Lab 2: Compare Prompt, Context and Harness Controls

Turn an ambiguous request into a measurable task contract and a minimal context package for an agent.

#### Detailed procedure

1. Read scenario.md and highlight the business outcome, prohibited actions and missing evidence.
2. Run the ambiguous prompt once in a fresh session and record why the result cannot be accepted.

   ```bash
   hermes
   ```

3. Complete task-contract.md with outcome, inputs, authority, acceptance evidence, stop conditions and rollback.
4. Edit AGENTS.md so the agent receives the fictional organisation rules at session start.
5. Start a fresh session in this folder and give the improved task contract.

   ```bash
   hermes
   ```

6. Compare the two outputs using acceptance-rubric.md; do not reward verbosity.
7. Remove any sensitive or credential-like content from the transcript and save only the evidence needed for review.
8. Run the verifier and explain which improvement came from prompting and which came from context engineering.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** The improved run names its evidence, respects the no-send rule and passes every acceptance item; the learner distinguishes prompt wording from context and runtime authority.

### Lab 3: Demonstrate Tools and an MCP Design Boundary

Use file and terminal tools for a grounded calculation, then design a least-privilege MCP connection without live credentials.

#### Detailed procedure

1. Inspect mock-tickets.csv and data-dictionary.md. Confirm the data is fictional.
2. Ask Hermes to calculate ticket count, median resolution time and breach rate using a terminal or code-execution tool.

   ```bash
   hermes chat --toolsets file,terminal
   ```

3. Require the agent to save analysis.md and include the calculation method.
4. Run independent-check.py and compare its result with the agent output.

   ```bash
   python3 independent-check.py
   ```

5. Complete mcp-design-template.md for a hypothetical CRM server: transport, scopes, read/write tools, trust tier and approval rules.
6. Mark every write-capable MCP tool as approval-required and exclude customer secrets from prompts and logs.
7. Record one failed or blocked tool call and identify whether the owning boundary was schema, permission, execution or evidence.
8. Run the bundle verifier.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** Independent calculations match the reported metrics, every claim points to the mock file, and the MCP design exposes only necessary capabilities.

### Lab 4: Demonstrate Memory Skills and Context Reuse

Separate durable business memory from reusable procedural skills and verify both on a new fictional case.

#### Detailed procedure

1. Read memory-candidates.md. Classify each item as durable memory, task context, skill instruction or prohibited secret.
2. Save only the approved durable fictional preferences using Hermes memory; never save the token-shaped marker.

   ```bash
   hermes chat --toolsets memory,skills,file
   ```

3. Create or revise a local skill from skill-template.md for evidence-led campaign briefing.
4. Inspect the skill trigger, scope, method, verification and stop conditions.
5. Start a fresh session with new-case.md and load the skill.

   ```bash
   hermes
   ```

6. Verify the new output uses durable preferences but does not copy transient facts from the first case.
7. Correct one fictional preference, rerun the test and record the before/after behaviour.
8. Complete memory-decision-log.md and run the verifier.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** The second case demonstrates durable preference reuse, procedural skill reuse, correction and zero secret or transient-noise retention.


## Topic 4: Multi-Agent Campaign Orchestration

Design specialist agents for marketing and video campaigns with isolated context, structured handoffs and a human-controlled release boundary.

### Delegation sequence

1. Coordinator defines bounded tasks
2. Specialists work in isolated contexts
3. Each returns evidence and artifacts
4. Reviewer challenges gaps
5. Human approves release

### Specialist role contract

- **Mission** — One clear output and audience.
- **Inputs** — Approved sources and context package.
- **Tools** — Minimum capabilities for the role.
- **Handoff** — Schema, evidence and failure status.

### Parallel and sequential work

- **Parallel:** Independent research strands; Lower elapsed time; Needs normalised handoffs; Conflicts resolved later
- **Sequential:** One output feeds the next; Clear dependency chain; Longer elapsed time; Earlier errors can propagate

### Marketing campaign agent team

1. Research agent gathers evidence
2. Audience agent builds segments
3. Strategy agent selects proposition
4. Creative agents draft variants
5. Compliance reviewer and human release

### Multi-agent marketing command center

A campaign becomes an evidence-linked pipeline, not one oversized prompt.
- Research before claims
- Specialists challenge each other
- Publication remains human-authorised

### Campaign handoff schema

- **Claim** — Exact statement and supporting source.
- **Audience** — Need, context and exclusion.
- **Asset** — Channel, copy, dimensions and owner.
- **Decision** — Approve, revise or reject with rationale.

### Illustrative variant score

Low risk score is desirable; the review gate balances performance with claim and brand exposure.

### Video campaign agent team

1. Brief and rights intake
2. Research and script
3. Storyboard and shot design
4. Generation and edit plan
5. QC, consent and human release

### Multi-agent video production studio

Video agents coordinate creative artifacts, but consent, rights and release remain human decisions.
- Traceable asset manifest
- Separate factual and visual QA
- No unapproved likeness or music

### Video production evidence

- **Storyboard** — Scene objective, framing and continuity.
- **Asset register** — Source, licence, consent and generation prompt.
- **QC report** — Audio, captions, factual claims and brand checks.
- **Release record** — Approved version, owner, date and destination.

### Generated preview and approved deliverable

- **Preview:** Explores concept; Watermarked or internal; May use placeholders; Not externally published
- **Deliverable:** Rights and consent cleared; Claims verified; Accessibility checked; Named human approval

### Conflict resolution between agents

1. Detect contradictory handoffs
2. Return both claims and evidence
3. Reviewer evaluates source quality
4. Coordinator revises synthesis
5. Human resolves consequential ambiguity

### Orchestration failure modes

- **Context leak** — Specialist receives unrelated sensitive data.
- **Silent dependency** — Downstream work starts before required evidence.
- **Consensus illusion** — Several agents repeat the same unsupported claim.
- **Release drift** — Draft moves outward without final approval.

### Coordination cost grows with handoffs

Add specialists only when role separation or parallelism creates more value than coordination overhead.

### Lab 5: Orchestrate Specialist Subagents

Split one campaign problem into isolated research, audience and risk tasks with structured evidence handoffs.

#### Detailed procedure

1. Read campaign-brief.md and define three independent specialist outputs.
2. Complete task-graph.md with parents, dependencies, acceptance criteria and stop conditions.
3. Use delegate_task in Hermes or the trainer demonstration to run research, audience and risk specialists in isolated contexts.

   ```bash
   hermes chat --toolsets file,web,delegation
   ```

4. Require every specialist to return the handoff schema in handoff-template.md.
5. Do not give specialists publication, messaging or spending tools.
6. Compare handoffs. If claims conflict, keep both evidence trails and route them to the reviewer.
7. Synthesize only after all parent tasks are complete; record missing evidence as a blocker.
8. Complete human-decision.md and run the verifier.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** Three role-bounded handoffs exist, conflicts remain visible, the synthesis waits for dependencies and the human decision record controls release.

### Lab 7: Create a Marketing Campaign with Multiple AI Agents

Coordinate research, audience, strategy, copy and review agents to produce a source-backed campaign pack that stops before publication.

#### Detailed procedure

1. Read product-evidence.md, brand-rules.md and audience-data.csv. Treat all facts as fictional classroom data.
2. Create a coordinator task that assigns research, audience, proposition, creative and risk-review roles.

   ```bash
   hermes chat --toolsets file,web,delegation,skills
   ```

3. Give each specialist only the files it needs and the handoff schema in campaign-handoff.md.
4. Require the research agent to map every factual claim to a supplied source line or label it assumption.
5. Require the audience agent to define inclusion and exclusion without sensitive inference.
6. Require the strategy agent to propose one measurable hypothesis and the creative agent to draft email, social and landing-page variants.
7. Route all variants to the risk reviewer for claim, rights, privacy and brand checks.
8. Assemble campaign-pack.md only after every handoff has passed or has an explicit blocker.
9. Complete approval-record.md. Do not send, publish, buy media or modify a CRM.
10. Run the verifier and conduct a peer challenge of one claim and one audience assumption.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** The campaign pack contains three differentiated channel drafts, a traceable evidence map, an experiment hypothesis, visible unresolved assumptions and human-controlled release.

### Lab 8: Create a Governed Multi-Agent Video Campaign

Produce a review-ready video campaign package with specialist agents, rights and consent controls, security tests and a human release gate.

#### Detailed procedure

1. Read approved-campaign-input.md. Confirm no real person, customer, copyrighted music or external publication destination is authorised.
2. Delegate script, storyboard, asset, factual-review and accessibility tasks with isolated context packages.

   ```bash
   hermes chat --toolsets file,delegation,skills
   ```

3. Require the script agent to use only approved product claims and include a clear call to action without deceptive urgency.
4. Require the storyboard agent to define six scenes with framing, action, duration and continuity notes.
5. Complete asset-rights-register.csv for every generated or supplied asset, including prompt, owner, licence, consent and allowed use.
6. If a trainer-approved video tool is available, create an internal low-resolution preview only. Otherwise complete generation-plan.md without calling an external service.

   ```bash
   hermes chat --toolsets file,delegation,video_gen
   ```

7. Run factual, visual, audio, caption and brand QC; record failures and required revisions in qc-report.md.
8. Complete security-boundary-test-matrix.md with negative tests for unapproved data, external send, unsafe URL, secret-like marker and unauthorised likeness.
9. Apply the human release checklist. Keep the decision at revise unless every rights, consent, factual and accessibility item passes.
10. Remove temporary media and credentials, run the verifier and retain only redacted evidence.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** The production package is complete and traceable, no unapproved asset or claim is used, negative controls block unsafe actions, and only a named human can approve final release.


## Topic 5: Security Governance and Implementation

Apply security, data governance, human oversight and continuous evaluation to turn a promising agent workflow into an accountable business process.

### Agent attack surface

- **Instructions** — Prompt injection and conflicting authority.
- **Data** — Sensitive input, poisoned retrieval and leakage.
- **Tools** — Over-privileged actions and unsafe arguments.
- **Supply chain** — Untrusted skills, plugins and MCP servers.

### Security enforcement order

1. Authenticate sender and profile
2. Classify data and task
3. Filter capabilities and paths
4. Require approval for impact
5. Execute in isolation and record evidence

### Model refusal and runtime control

- **Model refusal:** Probabilistic behaviour; May vary by provider; Useful defence in depth; Not proof an action was blocked
- **Runtime control:** Deterministic policy check; Observable allow or deny; Applies before execution; Produces auditable evidence

### Least-privilege design

- **Identity** — One profile and sender route per operating role.
- **Data** — Only approved files, fields and retention.
- **Capability** — Only required tools and endpoints.
- **Time** — Temporary approvals and credentials expire.

### Prompt-injection defence

1. Treat external content as data
2. Separate authority from retrieved text
3. Restrict tools before browsing
4. Validate target and arguments
5. Require approval for external effect

### Data governance lifecycle

- **Collect** — Purpose, lawful basis and minimum fields.
- **Process** — Approved provider, tools and locations.
- **Persist** — Session, memory, logs and access owners.
- **Delete** — Retention trigger and verifiable removal.

### Residual risk after layered controls

Layered controls reduce exposure; monitoring is still required because no layer removes all risk.

### Human oversight roles

- **Requester** — Defines need and permitted data.
- **Operator** — Configures agent and watches execution.
- **Reviewer** — Challenges evidence and output quality.
- **Accountable owner** — Accepts residual risk and release decision.

### AI incident response

1. Stop execution and external delivery
2. Preserve redacted evidence
3. Classify owning boundary
4. Apply approved minimum repair
5. Retest and record lessons

### Monitor outputs and outcomes

- **Output metrics:** Factual accuracy; Format completeness; Tool success; Latency and cost
- **Outcome metrics:** Cycle-time change; Customer or user effect; Review burden; Risk events and reversals

### Implementation workstreams

- **Process** — Future-state design and exception handling.
- **People** — Roles, training and change adoption.
- **Technology** — Integration, evaluation and support.
- **Governance** — Risk acceptance, audit and review cadence.

### Pilot-to-scale decision

1. Run bounded pilot
2. Measure value and failure modes
3. Close control gaps
4. Approve operating model
5. Scale gradually with rollback

### Human body and agent harness under stress

- **Human recovery:** Pause and seek help; Use judgement and values; Learn from feedback; Remain accountable
- **Agent recovery:** Stop condition and checkpoint; Ask for clarification or approval; Restore known state; Return evidence to accountable human

### Release gate evidence

- **Identity** — Correct course, profile, owner and destination.
- **Integrity** — Current artifact version and acceptance tests.
- **Privacy** — No secrets, personal data or trainer-only content.
- **Preservation** — Unrelated records and systems remain unchanged.

### Lab 8: Create a Governed Multi-Agent Video Campaign

Produce a review-ready video campaign package with specialist agents, rights and consent controls, security tests and a human release gate.

#### Detailed procedure

1. Read approved-campaign-input.md. Confirm no real person, customer, copyrighted music or external publication destination is authorised.
2. Delegate script, storyboard, asset, factual-review and accessibility tasks with isolated context packages.

   ```bash
   hermes chat --toolsets file,delegation,skills
   ```

3. Require the script agent to use only approved product claims and include a clear call to action without deceptive urgency.
4. Require the storyboard agent to define six scenes with framing, action, duration and continuity notes.
5. Complete asset-rights-register.csv for every generated or supplied asset, including prompt, owner, licence, consent and allowed use.
6. If a trainer-approved video tool is available, create an internal low-resolution preview only. Otherwise complete generation-plan.md without calling an external service.

   ```bash
   hermes chat --toolsets file,delegation,video_gen
   ```

7. Run factual, visual, audio, caption and brand QC; record failures and required revisions in qc-report.md.
8. Complete security-boundary-test-matrix.md with negative tests for unapproved data, external send, unsafe URL, secret-like marker and unauthorised likeness.
9. Apply the human release checklist. Keep the decision at revise unless every rights, consent, factual and accessibility item passes.
10. Remove temporary media and credentials, run the verifier and retain only redacted evidence.

   ```bash
   python3 verify.py
   ```


**Acceptance test:** The production package is complete and traceable, no unapproved asset or claim is used, negative controls block unsafe actions, and only a named human can approve final release.


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
