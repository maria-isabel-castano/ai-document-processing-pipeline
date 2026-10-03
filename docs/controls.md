# Operational controls

## Before AI
Confirm the document belongs to the expected workflow, enforce file/type/size constraints and assign a traceable document ID.

## After AI
Never treat model output as inherently valid. Parse into a schema, validate required fields and apply deterministic business rules.

## Confidence
A confidence score is a routing signal, not proof of correctness. Thresholds should reflect the cost of an incorrect automated action.

## Human review
Send exceptions with the source document, extracted fields, reason for review and a clear resolution action.

## Auditability
Persist the extraction version/model, validation outcome, routing decision and final human/system action where the business process requires traceability.
