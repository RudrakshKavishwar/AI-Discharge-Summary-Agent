from pydantic import BaseModel
from typing import List

class Medication(BaseModel):
    name: str
    dose: str
    frequency: str
    duration: str

class MedicationChange(BaseModel):
    medication: str
    change_type: str
    reason: str

class DischargeSummary(BaseModel):
    demographics: dict
    admission_date: str
    discharge_date: str

    diagnoses: List[str]

    hospital_course: str

    procedures: List[str]

    discharge_medications: List[Medication]

    medication_changes: List[MedicationChange]

    allergies: List[str]

    followup_instructions: List[str]

    pending_results: List[str]

    discharge_condition: str

    conflicts: List[str]

    missing_fields: List[str]