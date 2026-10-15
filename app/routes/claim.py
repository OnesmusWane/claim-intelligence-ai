from fastapi import APIRouter
from app.services.ai_service import process_claim_text

router = APIRouter(prefix="/claim", tags=["Claim"])

@router.post("/process")
def process_claim(payload: dict):
    text = payload.get("text", "")
    result = process_claim_text(text)
    return result