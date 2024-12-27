from fastapi import APIRouter, HTTPException, Request
import requests
from config import API_KEY

router = APIRouter()

@router.get("/test")
async def test_endpoint():
    return {"message": "LinkSquares API working!"}

@router.get("/proxy/agreements/{agreement_id}/tags")
async def proxy_agreement_tags(agreement_id: str):
    """
    Proxy to fetch agreement tags from LinkSquares API.
    """
    url = f"https://api.linksquares.com/api/analyze/v1/agreements/{agreement_id}/tags"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=response.status_code, detail=str(e))