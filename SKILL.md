---
name: scoping-review-cti
description: >
  Plan, execute, document, and report scoping reviews of empirical evidence on
  science, technology, and innovation policies or strategies in health and
  medicine. Builds reproducible searches, supports human-plus-AI screening,
  creates extraction and PRISMA-ScR artifacts, and maps policy evidence.
metadata:
  version: "0.1.0"
  platform: codex
  task_type: open-ended
  data_access_level: raw
---

# Scoping Review CTI

Use this skill for a scoping review about empirical evidence on public policies,
strategies, programmes, or interventions that promote science, technology, and
innovation in health or medicine.

This skill is generalizable. The initial configuration is based on the thesis
project *Políticas para promover la innovación de base tecnológica en salud*.
The thesis is a starting configuration, not a source of fixed results.

## Scope defaults

- Framework: PCC, JBI scoping-review guidance, and PRISMA-ScR reporting.
- Population/actors: governments, public agencies, research institutions,
  universities, firms, health systems, and policy beneficiaries.
- Concept: empirical evidence about CTI policies and strategies in health or
  medicine, including science policy, technology policy, innovation policy,
  health-technology policy, industrial policy, and R&D policy.
- Secondary dimension: intellectual property, patents, licensing, technology
  transfer, access to medicines, and related instruments. Do not make IP a
  mandatory inclusion criterion unless the user changes the scope.
- Evidence: primary empirical studies and policy/strategy documents with
  observable evidence. Exclude purely theoretical or conceptual papers.
- Exclude: social innovation without a technological or CTI-policy component;
  health-technology-assessment-only studies; and records without accessible
  full text when full-text eligibility is required.
- Default limits: no date, language, or geographic restriction. Record the
  actual search date and any user-imposed limits.

## Modes

1. `intake`: convert the topic into PCC, objectives, review questions, and
   eligibility criteria.
2. `search`: build database-specific equations and a search log for Scopus,
   Web of Science, PubMed/MEDLINE, and optional institutional repositories.
3. `screen`: deduplicate, pilot, and manage title/abstract and full-text
   decisions. Treat the AI as reviewer 1 and a named human as reviewer 2; the
   human must resolve or validate disagreements before final inclusion.
4. `extract`: create and maintain the evidence-extraction matrix, preserving
   source locators and separating reported findings from interpretation.
5. `synthesize`: map countries, policy levels, policy-cycle stages, instruments,
   implementation, outcomes, barriers, facilitators, and the secondary IP
   dimension. Do not infer policy effectiveness from policy description alone.
6. `report`: produce PRISMA-ScR counts, exclusion reasons, evidence tables, and
   draft methods/results text. Clearly mark planned, screened, extracted, and
   validated states.

## Mandatory workflow gates

- Freeze the review question and eligibility criteria before full screening.
- Pilot at least 30 title/abstract records when the corpus permits; record the
  agreement rule and changes to the criteria.
- Use one mutually exclusive primary exclusion reason per record for PRISMA
  accounting, with optional secondary notes.
- Preserve both reviewers' decisions, disagreement status, and adjudication.
- Record database, platform, date, complete query, filters, and result count.
- Keep an audit trail for deduplication and full-text availability.
- Cite the exact document or page/section locator for extracted claims whenever
  possible. Never fabricate a reference, policy, result, or impact estimate.
- Do not call a policy effective, successful, or high-impact unless the source
  provides empirical support and the synthesis explains its design and limits.

## Deliverables

Use the templates in `assets/` and the schemas in `references/` when the user
asks for files. The minimum package is:

- protocol/intake brief;
- database-specific search equations and search log;
- deduplicated record file;
- title/abstract screening file;
- full-text screening and exclusion-reason file;
- evidence-extraction matrix;
- PRISMA-ScR count table;
- narrative and descriptive evidence map.

## References to load conditionally

- Read `references/methodology_cti.md` for PCC, inclusion/exclusion, reviewer
  roles, and synthesis rules.
- Read `references/search_equations.md` when building or revising searches.
- Read `references/extraction_schema.md` when creating or modifying a matrix.
- Read `references/prisma_artifacts.md` when calculating flow counts or writing
  the report.

## Human boundary

The AI may propose searches, classify records provisionally, identify conflicts,
and populate draft extraction fields. A human researcher must validate the
eligibility criteria, adjudicate disagreements, approve the final corpus, and
approve substantive interpretations.

