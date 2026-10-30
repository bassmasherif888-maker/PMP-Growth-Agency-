# Current delivery

[Revised lean guide and deck: English & Egyptian Arabic](lean/) — 5-page guide, 10-slide briefing, editable Word/PowerPoint and PDF previews. Supersedes the previous long delivery.

## Incoming Marketing Manager onboarding

For detailed daily operation and training, use the [manager onboarding pack](onboarding/index.html): editable runbook, 48-slide training deck, PDF previews, templates and scenario answer keys. This is separate from the concise owner handover below. Includes company resource restrictions, shoot coordination and equipment accountability; unconfirmed controls remain labeled.

## Primary owner handover pack

The latest goal is the Marketing Department Mode of Operations / SOP for owner handover. Use [the editable operating manual](handover/PMP-Marketing-Department-Owner-Handover-SOP.docx), [the concise editable owner briefing](handover/PMP-Marketing-Department-Owner-Handover.pptx), and [the handover download page](handover/index.html). The earlier long presentation and browser application remain supporting reference/demo materials. See [handover notes](handover/README.md) for scope and rebuilding.

# PMP Growth OS

A working, dependency-free agency operations demo: command center, 14-position organization explorer, nine editable workflow journeys, seven-checkpoint campaign simulation, Kanban task board, role academy and computed workload dashboard.

## Run

Requires Node.js 24 or later. No package downloads, credentials or external services are required.

```sh
npm run dev
```

The server listens on port 3000 (override with `PORT`).

```sh
npm run check
npm test
npm run build
SERVE_DIST=1 npm start
```

`build` creates standalone assets in `dist/`. This implementation deliberately uses native browser ES modules and Node's standard library because the cloud network proxy was unavailable during the build. It does not use Next.js, TypeScript or React. Syntax checks are not TypeScript type checks.

## Try it

- Open Organization Map. Inspect any role, change its manager or drag it onto another position. Cyclic reporting lines are rejected. Graphic designers and video editors have separate position IDs.
- Open Workflow Journey to choose or edit one of nine templates. Click handoff arrows for sender, receiver, artifacts, rationale, timing and acceptance rules.
- Open Mission Control and resolve all seven decision gates. Play pauses for user decisions; incorrect choices explain why the gate remains held. Score is one illustrative point per correctly resolved checkpoint.
- Create a task, assign one accountable owner, mark inputs received, and move it through the task board. Incomplete dependencies block handoffs. Internal/client approvals precede publication; media launch also needs budget authorization.
- Open task details to record simulated independent approvals or return work with actionable revision feedback. Reassigning clears approvals.
- Open Performance to inspect active workload and upstream dependency signals.

## Scope and assumptions

All campaigns, clients, tasks, scores and notifications are fictional DEMO data. No real spending, publication, messages or client authorization occurs. Approval actions explicitly simulate the displayed reviewer. This is not a secure authorization system.

Video Editor 1 and Video Editor 2 report directly to the Marketing Manager, confirmed by the user. Other reporting lines, review policies and workflows are proposed and editable. Coordination by Account Management does not imply line-management authority. Automated escalation is off; no confirmed SLAs, monetary impacts, real deadlines or capacity limits are assumed.

Official PMP brand assets could not be accessed. The text wordmark, lime/forest palette and system typography are **temporary**, not verified PMP identity. Replace `brand-tokens.js` and centralized CSS theme tokens after official assets are supplied. Light/dark themes, reduced-motion styles, keyboard focus indicators and responsive layouts are included.

State persists in localStorage in the same browser. Settings supports JSON export and demo reset. Browser storage is not a shared database, secure audit trail, authentication system or backup. Data is local and may be cleared by the browser.

## MVP limitations and next work

Workflow templates currently have editable ordered stages with explanatory conditional routing; a general executable branch/parallel workflow editor is not implemented. The simulator is a guided seven-checkpoint scenario, not a production scheduling engine. The organization visualization supports pointer pan, zoom, fit-to-view, keyboard navigation, role search, department filters, five relationship layers, clickable edge explanations and drag-to-reparent. Search automatically focuses matching positions. A mobile position directory provides readable role access alongside the zoomable map. Task due dates, business-calendar forecasting, attachments, editable approval-policy configuration and additional exception missions remain future work. Analytics intentionally omit turnaround, overdue and client-performance numbers until corresponding data exists.

For production: migrate to typed components if desired; add authenticated backend storage, server-enforced role permissions, actual client approval records, tamper-resistant history, workflow branch validation and real integration adapters. Keep provisional company policies separate from verified operational rules.

## Validation

Twenty-three Node tests cover distinct role seeds, reporting/dependency cycles, required inputs, publishing approvals, budget gates, independent review, revisions full mission completion, graph layout and all five relationship layers. Browser smoke checks exercise navigation, all 14 org cards, inspectors, task creation, mission completion, reload persistence and mobile viewport fit.

## Confirmed delivery process and workbook structure

The Account Manager attends client meetings, writes and distributes the brief to Content, Design and Editing, assigns tasks and monitors execution. Content and Design heads perform team quality review; Marketing Manager performs video quality review and supplies the subsequent internal approval. The Account Manager then collects finalized deliverables into one PPTX, presents it for final client approval and passes the approved presentation to Social Media Specialist for scheduling/publication.

AM, Marketing Manager and the relevant head can each record actionable comments. The task remains open until its accountable holder executes every comment and records a response. Re-review and Marketing approval are required after rejection. New revisions invalidate the project presentation and block publication until it is reassembled and client-approved.

Social Media Specialist gathers private-label calendars, creates strategies, performance reports and listening reports, schedules/publishes approved calendars and replies to comments on private-label pages.

Task-sheet-inspired fields include brief, account, priority, owner, deadline, start/end dates, deliverable references, creative/revision references and holder notes. Historical spreadsheet labels such as First approval and Final approval do not prove which actor approved or that the client approved. No real staff/client records, private links, workbook rows or credentials are imported into this public demo.

The demo exports a native editable PPTX of task summaries after reviews pass. Actual creative files are not attached or embedded; this is not a complete real-client presentation until the approved deliverable assets are added. All approvals are local simulations. Existing browser tasks are retained on process migration, but obsolete approvals are reset so the new gates cannot be bypassed. Shared persistence and authenticated reviewer permissions still require a backend.

## Client folder lifecycle and work submission

Before a contract is signed, the client folder is inside the main `PMP Drive / Quotations` folder. When the client signs, Sales or Business Developer moves that same folder out to `PMP Drive / [Client name]`, retaining its contents. It is moved, not duplicated. The standalone client folder holds Quotation documents, Start Strategy, Client Brief, Content with monthly calendar PPTX files, Design with monthly final-approved designs, Videos with monthly final-approved videos, and other scope-specific work. The Account Manager opens the kickoff WhatsApp group with client, PMP owner, Marketing Manager and relevant stakeholders. These group participants do not create additional positions in the 14-role map.

Content submits work on the task sheet and uploads its working calendar PPTX to Drive, receiving comments on that same calendar. Design and Video monthly folders contain only final internally and client-approved copies. Their draft-review location is not specified. Monthly `[YYYY-MM]` labels are a suggested naming convention, not a confirmed historical folder format. The website guide documents the process; it does not create real Drive folders, groups or uploads.

## Commercial journey before delivery

Sales or Business Developer leads acquisition through on-ground visits, researched cold calls, LinkedIn, email campaigns and calls to leads from PMP paid media. Account Manager participates throughout. Before the first online/offline meeting, prepare and study the audit, strategy and a three-tier suggested quotation. If the prospect is convinced, request a second meeting with printed client brief, strategy, agreed quotation and contract; the client signs all four. Contract signing moves the existing folder out of Quotations; actual delivery readiness also requires the upfront payment. Social-management-only contracts require 100% upfront. Contracts including other services require 50% upfront. The media-buying fee (described by the user as a 25% retainer) is calculated after plan execution on actual media expenses. No new balance-payment timetable, ad-spend funding or tax rule is assumed.

Supplied SKILL-1.md is the SSM Strategy framework: confirm scope/format/language/access, research, identify contradictions, label Observed/Interpretation/Recommendation, disclose verification gaps, and complete all 26 sections when a full strategy is in scope. It does not contain an agency quotation formula or current rates. Three tiers need verified market-range and prior-price evidence, proposed scope, client industry and class. Public view patterns alone do not establish paid boosting. No client audit, actual market rates or prices are fabricated. The raw skill and internal pricing evidence are not published.

The website includes a separate local readiness calculator for illustrative contract-payment checks. It does not verify bank transfers, sign contracts, authorize actual project work or enforce commercial gates across a production system. Actual delivery approval and finance controls need authenticated backend integration.

The latest editable operating-process deck is `presentations/PMP-Growth-OS-Full-Client-Journey-Editable.pptx` (59 slides); `PMP-Growth-OS-Full-Client-Journey.pdf` provides a read-only preview. Montserrat and Bebas Neue are the intended fonts, as specified by the supplied branding direction. The presentation was rendered and checked for layout; it is a process guide, not a completed client strategy.

## Post-meeting strategy alignment gate

Meeting one alone does not start actual-strategy development. Only after meeting one AND the client confirms readiness to sign does AM compare Sales/BD’s skill-generated pre-meeting proposal strategy with the actual meeting brief. AM then develops the actual strategy with Social Media Specialist, Marketing Manager and Media Buyer. Actual strategy informs the second-meeting printed signing pack and any quotation scope adjustments. If the client is not ready to sign, actual-strategy work stays pending. This readiness gate precedes actual signature; contract signing still triggers the folder move, and the required upfront payment still gates delivery.


## English and Arabic deliverables

[Download all final outputs in both languages](arabic/) — editable owner handover, detailed manager onboarding and full journey reference, including monthly performance appraisals.
