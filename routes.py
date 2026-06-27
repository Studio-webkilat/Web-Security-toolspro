from fastapi import APIRouter
from models import SecurityScanRequest, SecurityResponse
import requests

router = APIRouter()

@router.post("/scan", response_model=SecurityResponse)
async def run_security_scan(request: SecurityScanRequest):
    target = str(request.target_url)
    
    try:
        # Mengambil header dari website target
        response = requests.get(target, timeout=5)
        headers = response.headers
        
        # Daftar header keamanan yang dicari
        security_headers = [
            'Content-Security-Policy',
            'X-Frame-Options',
            'X-Content-Type-Options',
            'Strict-Transport-Security'
        ]
        
        found = {h: (h in headers) for h in security_headers}
        
        return {
            "status": "success",
            "message": f"Scan selesai untuk {target}",
            "data": {"found_headers": found}
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Gagal memindai target: {str(e)}",
            "data": {}
        }
