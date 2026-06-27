from fastapi import APIRouter
from models import SecurityScanRequest, SecurityResponse

router = APIRouter()

@router.post("/scan", response_model=SecurityResponse)
async def run_security_scan(request: SecurityScanRequest):
    return {
        "status": "success",
        "message": f"Scan dimulai pada {request.target_url}",
        "data": {"scan_id": "12345", "type": request.scan_type}
    }
