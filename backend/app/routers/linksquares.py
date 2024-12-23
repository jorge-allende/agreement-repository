import os
import requests
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

router = APIRouter()

# API Key and Base URL
API_KEY = os.getenv("LINKSQUARES_API_KEY")
BASE_URL = "https://api.linksquares.com/api/analyze/v1/agreements"

if not API_KEY:
    raise RuntimeError("LINKSQUARES_API_KEY is not set. Please check your .env file.")

@router.get("/linksquares/agreements")
async def get_agreements():
    """
    Fetch agreements from LinkSquares API.
    """
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,  # API Key as required in the headers
    }

    try:
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()  # Return the JSON response from LinkSquares
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")
