# AI Document Processing Pipeline

A reference workflow for using AI inside an operational document process without treating the model as the entire system.

The pipeline separates deterministic controls from AI-assisted extraction and keeps low-confidence or invalid outputs on a human-review path.

## Architecture

```text
Document Intake
      ↓
Pre-validation
      ↓
Extraction Layer (AI-capable)
      ↓
Schema Validation
      ↓
Confidence / Business Rules
   ↙                 ↘
Auto Process       Human Review
   ↘                 ↙
     Operational Action
            ↓
         Audit Log
```

## What it demonstrates

- AI as one component of a workflow
- structured extraction contract
- deterministic validation after extraction
- confidence thresholds
- human-in-the-loop exceptions
- audit-friendly decisions
- synthetic documents/data only

## Quick start

Requires Python 3.10+.

```bash
python src/pipeline.py
```

The demo extractor is deterministic and local. In production it can be replaced by an LLM/document AI adapter while keeping validation, routing and audit logic stable.

## Design principle

**System → Automation → AI → Human**

Use ordinary software for deterministic rules. Use AI where interpretation adds value. Keep humans responsible for exceptions where confidence or business risk requires judgment.

## Related

- [Portfolio](https://mariacastano.co/)
- [AI Automation](https://mariacastano.co/ai-automation/)
- [How to Prepare a Business Workflow for AI Automation](https://mariacastano.co/insights/prepare-workflow-for-ai/)

Built by **María Isabel Castaño — AI Systems Developer | Web Apps, APIs & Automation**.
