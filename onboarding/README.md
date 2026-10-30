# Detailed incoming Marketing Manager onboarding pack

A separate operational training manual, not a replacement for the private client files/task sheet or the concise owner handover.

- `PMP-Incoming-Marketing-Manager-Detailed-Runbook.docx` — editable detailed manual: gate reasoning, first-30-days plan, 14-role map, tools/access, sheet interpretation, daily/weekly routines, 13 procedure playbooks with manager checks, quality rubrics, exception routes, reporting, worked example, 14 reusable templates, 16 scenarios/answer keys and open decisions.
- Matching Markdown contains the complete document body/tables in order.
- `PMP-Incoming-Marketing-Manager-Detailed-Onboarding.pptx` — 48 native editable training slides.
- Matching PDFs are read-only previews with document heading navigation where supported.
- `index.html` is the public download page; `onboarding-content.json` contains the training lenses, worked cases, scenarios and templates.

Confirmed policy: Higgsfield is restricted to the two Video Editor positions, forbidden for all other team members. Claude/ChatGPT/Canva/Adobe are company-provided, but specific seat/licence assignments are not assumed. AM coordinates outsourced crew, guests and PR. SM collects/transfers source media, captures BTS and is fully accountable for memory cards/studio tools. Several hard drives exist; drive custody/backup policy remains unconfirmed.

Controls not specified by the user are marked recommended/to confirm. No private source files, passwords, client/staff records, actual pricing or performance data are included. The software access rule is documented, not technically enforced by this static pack. Training competence and live authority are not certified.

Rebuild from the repository root with `python3 onboarding/build_onboarding.py`; requires python-docx and python-pptx. Source procedure data is read from `handover/procedure-register.json` and the role list from `handover/build_handover.py` (AST parsing only). Refresh PDF previews with LibreOffice after installing Montserrat and Bebas Neue; review rendered pages. Run `python3 onboarding/validate_onboarding.py` after exports are updated.
