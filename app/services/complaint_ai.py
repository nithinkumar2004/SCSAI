from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class FormalComplaint:
    subject: str
    summary: str
    details: str
    category: str
    department: str
    requested_action: str
    keywords: List[str]
    created_at: str


def _detect_category(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ["police", "crime", "theft", "assault"]):
        return "Public Safety"
    if any(word in lowered for word in ["road", "street", "lights", "garbage", "water"]):
        return "Municipal"
    if any(word in lowered for word in ["tax", "refund", "income", "gst"]):
        return "Taxation"
    if any(word in lowered for word in ["hospital", "doctor", "ambulance", "clinic"]):
        return "Healthcare"
    return "General"


def _map_department(category: str) -> str:
    return {
        "Public Safety": "Police Department",
        "Municipal": "Municipal Corporation",
        "Taxation": "Revenue Department",
        "Healthcare": "Health Department",
        "General": "District Administration",
    }.get(category, "District Administration")


def generate_formal_complaint(summary: str, details: str) -> FormalComplaint:
    combined = f"{summary} {details}".strip()
    category = _detect_category(combined)
    department = _map_department(category)
    keywords = [word.strip(".,") for word in combined.split() if len(word) > 4][:8]
    requested_action = (
        "Please investigate and resolve the issue promptly with status updates shared to the citizen."
    )
    created_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return FormalComplaint(
        subject=summary or "Citizen Grievance",
        summary=summary or "A citizen has reported an issue requiring attention.",
        details=details or "Additional details will be provided upon request.",
        category=category,
        department=department,
        requested_action=requested_action,
        keywords=keywords,
        created_at=created_at,
    )
