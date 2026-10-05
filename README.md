# Lab 03
## Using AI & LLMs in the Software Planning Phase

**Primary Configuration Key:** `SCOPE_LEDGER`
**Course:**  Software Construction and Development

---

## 1. Lab Overview

This laboratory exercise demonstrates how Artificial Intelligence (AI) and Large Language Models (LLMs) can support the software planning phase.

The selected system for this lab is a:

**Campus Event Management System**

The original stakeholder brief is:

> "Students browse events, register, and get reminders; admins add and remove events."

The planning process was performed by converting this short stakeholder brief into a traceable Work Breakdown Structure (WBS), a prioritised user-story backlog, a locally informed requirement, and an honest prompt ledger.

The main purpose was not simply to generate requirements using AI, but to **review, reconcile, and validate AI-generated planning outputs against the original stakeholder brief**.

---

# 2. Objectives

The main objectives of this laboratory were:

* Generate a Work Breakdown Structure (WBS) from a short stakeholder brief.
* Maintain hard traceability between requirements and their source.
* Identify AI-generated scope that is not supported by the stakeholder brief.
* Identify requirements that were missing from an initial AI-generated plan.
* Convert the reconciled WBS into user stories.
* Prioritise user stories using the MoSCoW method.
* Identify a requirement based on local campus/device context.
* Maintain an honest record of prompts used during planning.
* Demonstrate Git-based versioning of the planning artifacts.
* Understand where AI is useful and where human validation is necessary.

---

# 3. System Scope

## Campus Event Management System

The system is intended to support campus event management.

### Student Functions

Students should be able to:

* Browse available campus events.
* Register for events.
* Receive reminders about events.

### Administrator Functions

Administrators should be able to:

* Add new events.
* Remove events.

The original brief is intentionally short. Therefore, additional requirements were treated carefully rather than automatically becoming part of the confirmed scope.

---

# 4. Task 1 — Reconciled Work Breakdown Structure

### Submission Marker

`CSE325-2026-L03-T9WD-T1`

### Configuration Key

`SCOPE_LEDGER`

The WBS was reviewed against the exact wording of the stakeholder brief.

Each WBS item was classified as either:

* **Traceable** — directly supported by an exact phrase from the brief.
* **ADDED** — not directly stated in the brief and therefore requiring a clear reason for inclusion.

### Traceable Requirements

| WBS ID | Requirement                  | Source                     |
| ------ | ---------------------------- | -------------------------- |
| WBS-01 | Students browse events       | "students browse events"   |
| WBS-02 | Students register for events | "students register"        |
| WBS-03 | Students receive reminders   | "get reminders"            |
| WBS-04 | Admins add events            | "admins add ... events"    |
| WBS-05 | Admins remove events         | "admins ... remove events" |

### Additional Planning Items

Some planning considerations were identified as necessary during requirements analysis but were not explicitly stated in the original one-line brief.

| WBS ID | Item                      | Status | Reason                                                                                                                      |
| ------ | ------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| WBS-06 | Registration cancellation | ADDED  | A practical registration workflow should consider how a student can cancel an existing registration.                        |
| WBS-07 | Session/token handling    | ADDED  | Authentication/session security requires implementation consideration even though it is not explicitly stated in the brief. |

### Unsupported AI Scope

An unsupported example identified during the planning review was:

> "Create user accounts."

This requirement is not directly supported by the stakeholder sentence. It was therefore not accepted as a confirmed requirement.

### Result

The WBS was reconciled so that unsupported AI-generated scope was not silently treated as stakeholder-approved scope.

---

# 5. Task 2 — User Story Backlog and MoSCoW Prioritisation

### Submission Marker

`CSE325-2026-L03-T9WD-T2`

### Configuration Key

`SCOPE_LEDGER`

The reconciled WBS was converted into user stories.

The MoSCoW method was used to classify each story as:

* **Must** — essential for the system's core purpose.
* **Should** — important but not absolutely essential for the first release.
* **Could** — useful enhancement if time/resources permit.
* **Won't** — intentionally excluded from the current release.

## Backlog Summary

| ID    | User Story                                                                                                      | Priority |
| ----- | --------------------------------------------------------------------------------------------------------------- | -------- |
| US-01 | As a student, I want to browse campus events so that I can discover available events.                           | Must     |
| US-02 | As a student, I want to view event information so that I can understand an event before registering.            | Must     |
| US-03 | As a student, I want to register for an event so that I can attend it.                                          | Must     |
| US-04 | As a student, I want to receive event reminders so that I do not miss registered events.                        | Must     |
| US-05 | As an admin, I want to add events so that new campus events become available to students.                       | Must     |
| US-06 | As an admin, I want to remove events so that cancelled or invalid events are no longer available.               | Must     |
| US-07 | As a student, I want to cancel my registration so that I can withdraw from an event.                            | Should   |
| US-08 | As an admin, I want to view registered attendees so that I can manage event participation.                      | Should   |
| US-09 | As a student, I want to search or filter events so that I can find relevant events quickly.                     | Could    |
| US-10 | As an admin, I want to export attendee information so that I can use it for administrative purposes.            | Could    |
| US-11 | As a student, I want a notification when an event is cancelled so that I know the event is no longer available. | Won't    |
| US-12 | As an admin, I want an analytics dashboard so that I can analyse event participation.                           | Won't    |
| US-13 | The application should be tested on the actual Android 16 device available for local validation.                | Should   |

---

## MoSCoW Defence

### US-03 — Register for Event

**US-03 is Must** because registration is a core action explicitly required by the stakeholder brief.

It takes priority over **US-09 (Search/Filter)** because students can still browse events without advanced filtering, but the system cannot fulfil its registration purpose without registration.

### US-04 — Event Reminders

**US-04 is Must** because reminders are explicitly included in the stakeholder brief.

It takes priority over **US-10 (Export Attendee Information)** because reminders are part of the stated student-facing functionality, while exporting data is an additional administrative convenience.

### US-05 — Admin Add Events

**US-05 is Must** because administrators must be able to add events for the event catalogue to exist and remain useful.

It takes priority over **US-08 (View Attendees)** because viewing attendees is an additional administrative feature, while adding events is explicitly required by the original brief.

---

# 6. Task 3 — Local Context Requirement

### Submission Marker

`CSE325-2026-L03-T9WD-T3`

### Configuration Key

`SCOPE_LEDGER`

A local requirement was introduced based on the actual device available for testing.

### Local Context

The available testing device uses **Android 16**.

A generic LLM cannot reliably know which physical device is available to the student unless that information is explicitly provided.

Therefore, the following planning requirement was added:

> The application should be tested on the actual Android 16 device available for local validation.

### MoSCoW Priority

**Should**

### Why AI Cannot Determine This Automatically

An LLM can suggest common Android versions and testing practices, but it cannot know the student's actual physical device, installed operating system, campus network, or other local conditions without being told.

This demonstrates why human-provided local context is important during AI-assisted software planning.

---

# 7. Task 4 — Honest Prompt Ledger

### Submission Marker

`CSE325-2026-L03-T9WD-T4`

### Configuration Key

`SCOPE_LEDGER`

The prompt ledger records the planning prompts and explains how the planning process evolved.

## Prompt 1 — Initial Planning

**Prompt:**

> Plan a Campus Event Management System. Give me the tasks needed to build it.

**Result:**
The result was too general and did not provide sufficient traceability to the stakeholder brief.

**Action:** Superseded.

---

## Prompt 2 — Structured Planning

**Prompt:**

> Act as a software project planner. Break the Campus Event Management System into 4-6 modules. For each module list 3-5 concrete engineering tasks. Give the result as a nested list.

**Result:**
The output was more structured, but it still did not prove that every task came from the stakeholder brief.

**Action:** Superseded.

---

## Prompt 3 — Traceability

**Prompt:**

> Extract a reconciled WBS from the exact stakeholder brief. Every requirement must either include an exact quoted phrase from the brief or be labelled ADDED with a reason. Do not silently invent scope.

**Result:**
The WBS became traceable and unsupported scope could be separated from stakeholder requirements.

**Action:** Accepted.

---

## Prompt 4 — User Stories and MoSCoW

**Prompt:**

> Convert the reconciled WBS into at least 10 user stories. Assign each story a MoSCoW priority and explain why the Must stories are more important than competing stories. Do not mark every story as Must.

**Result:**
The requirements were converted into a prioritised backlog.

**Action:** Accepted.

---

## Prompt 5 — Critical Review

**Prompt:**

> Review the planning output as a critical requirements engineer. Identify missing requirements and failure cases, but clearly separate genuine planning gaps from requirements that would introduce unsupported scope.

**Result:**
The planning output was reviewed for omissions while avoiding uncontrolled scope expansion.

**Action:** Accepted.

---

## Prompt 6 — Local Context

**Prompt:**

> Identify one requirement that depends on information available to the student locally but cannot be reliably determined from the stakeholder brief alone. Do not invent the local fact. Explain why the LLM cannot know it and assign an appropriate MoSCoW priority.

**Result:**
A local testing requirement based on the available Android 16 device was identified and added to the backlog.

**Action:** Accepted.

---

# 8. Git Versioning

Git was used to maintain versions of the laboratory artifacts.

The repository contains the planning documents and supporting files.

Suggested commit sequence:

```text
L03 initial planning draft
L03 reconciled WBS
L03 MoSCoW backlog
L03 local-context requirement
L03 final submission
```

Git versioning provides evidence that the planning artifacts were developed and refined rather than produced as one untracked final document.

---

# 9. Deliverables

The Lab 03 submission contains the following files:

```text
LAB-03/
│
├── Lab03_WBS.docx
├── Lab03_Backlog.xlsx
├── Lab03_Local_Context.docx
├── Lab03_Prompt_Ledger.docx
└── README.md
```

### File Descriptions

**Lab03_WBS.docx**
Contains the reconciled WBS, traceability information, added items, and unsupported AI scope analysis.

**Lab03_Backlog.xlsx**
Contains the user-story backlog and MoSCoW prioritisation.

**Lab03_Local_Context.docx**
Documents the locally known Android 16 testing context and explains why an LLM cannot determine this fact automatically.

**Lab03_Prompt_Ledger.docx**
Documents the prompts and changes made during the AI-assisted planning process.

**README.md**
Provides an overall explanation of the laboratory work, methodology, scope reconciliation, and deliverables.

---

# 10. Key Learning Outcome

This laboratory demonstrates that AI/LLMs can significantly accelerate software planning, especially for:

* generating initial WBS structures;
* converting requirements into user stories;
* suggesting prioritisation;
* identifying possible omissions;
* reviewing planning artifacts.

However, AI-generated planning output should not automatically be treated as the final specification.

Human review is required to:

* verify stakeholder traceability;
* remove unsupported scope;
* provide local context;
* resolve ambiguity;
* validate priorities;
* confirm the final project scope.

The most important lesson is:

> **AI can assist the planning process, but human validation is required to establish the actual project scope.**

---

# 11. Scope Control

Throughout the planning process, the original stakeholder brief was treated as the primary scope boundary.

Requirements directly supported by the brief were retained as traceable requirements.

Additional requirements were explicitly marked as **ADDED** rather than being presented as if they came from the stakeholder.

This approach prevents accidental scope expansion caused by AI-generated assumptions.

---

# 12. Submission Reference

**Submission Reference:** `CSE325-2026-L03-T9WD`

**Task 1:** `CSE325-2026-L03-T9WD-T1`
**Task 2:** `CSE325-2026-L03-T9WD-T2`
**Task 3:** `CSE325-2026-L03-T9WD-T3`
**Task 4:** `CSE325-2026-L03-T9WD-T4`

**Primary Configuration Key:** `SCOPE_LEDGER`

Scope reconciled against the brief.

CSE 325-2026-L03-T9WD.
