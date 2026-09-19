---
name: lead-triage
description: Use when working the leads a website has captured — for example "any new leads", "who came in this week", "mark that lead contacted", "add a note to this enquiry", "what happened with the Johnson lead", or "how is the pipeline looking". Lists new leads from AdvisorSEO, opens one in full with its history, and moves leads through the pipeline with a note on each move.
---

# Triage and work the lead pipeline

Leads arrive from the website's contact form and land in AdvisorSEO. This skill reads
them, opens one, and moves it along. Both write steps preview first and change nothing
until called again with `confirm=true`.

## 1. List what is new

- `gravity_list_leads(site_id=..., status="new")` — newest first, with a stats summary
  of the pipeline. Spam-flagged leads are left out unless `include_spam=true`.
- Omit `site_id` to read across every site in the workspace.
- Omit `status` to see every stage at once.
- `limit` defaults to 50; raise it for a backlog.

Present the new leads as a short list: who, what they asked for, when it arrived. Put the
ones that look ready to buy at the top and say why.

## 2. Open one in full

- `gravity_list_leads(lead_id=...)` — that single lead in full, with its activity trail:
  every status change and every note, in order.

Read the trail before acting. It will often show the lead was already chased.

## 3. Move it along

- `gravity_update_lead(lead_id, status=..., note="...")` — preview, then `confirm=true`.
- Valid statuses are exactly: `new`, `contacted`, `qualified`, `converted`, `lost`.
  Anything else is rejected.
- `status` and `note` are both optional, but pass at least one. A status move with no
  note leaves the next person guessing — write what happened, in a sentence.
- The note appends to the activity trail; it never overwrites an earlier one.

Stage by stage:

- `contacted` — an outreach actually went out. Note the channel and the date.
- `qualified` — they answered and they fit. Note what they want and their budget signal.
- `converted` — they bought. Note what they bought.
- `lost` — note the reason, in their words where you have them.

Confirm each move with the person before calling with `confirm=true`, and never mark a
lead contacted on the assumption that someone will follow up later. The status is a
record of what happened, not of what is intended.

## 4. Report the pipeline

- `gravity_overview(site_id=...)` — lead totals, new, converted and spam counts, plus
  recent activity across the workspace.

Close with the pipeline shape and the single next action you would take.
