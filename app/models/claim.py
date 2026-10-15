from pydantic import BaseModel
from typing import Optional

class ClaimRequest(BaseModel):
    claim_id: str
    policy_number: str
    patient_name: str
    description: Optional[str] = None