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

Eleven Node tests cover distinct role seeds, reporting/dependency cycles, required inputs, publishing approvals, budget gates, independent review, revisions full mission completion, graph layout and all five relationship layers. Browser smoke checks exercise navigation, all 14 org cards, inspectors, task creation, mission completion, reload persistence and mobile viewport fit.
