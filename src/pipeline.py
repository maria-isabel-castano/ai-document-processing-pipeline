from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ExtractedDocument:
    document_id: str
    vendor: Optional[str]
    total: Optional[float]
    confidence: float


@dataclass
class Decision:
    route: str
    reason: str


def extract_demo(document_id: str, text: str) -> ExtractedDocument:
    """Deterministic stand-in for an AI extraction adapter."""
    vendor = "Northwind Supply" if "Northwind" in text else None
    total = 1240.50 if "1240.50" in text else None
    confidence = 0.96 if vendor and total is not None else 0.62
    return ExtractedDocument(document_id, vendor, total, confidence)


def validate(doc: ExtractedDocument) -> list[str]:
    errors = []
    if not doc.vendor:
        errors.append("vendor_missing")
    if doc.total is None or doc.total <= 0:
        errors.append("invalid_total")
    return errors


def route(doc: ExtractedDocument, threshold: float = 0.90) -> Decision:
    errors = validate(doc)
    if errors:
        return Decision("HUMAN_REVIEW", ",".join(errors))
    if doc.confidence < threshold:
        return Decision("HUMAN_REVIEW", "confidence_below_threshold")
    return Decision("AUTO_PROCESS", "validated_high_confidence_extraction")


if __name__ == "__main__":
    raw = "Invoice from Northwind Supply. Total due: 1240.50"
    extracted = extract_demo("DOC-1007", raw)
    decision = route(extracted)
    print({"extracted": asdict(extracted), "decision": asdict(decision)})
