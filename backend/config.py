import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("LINKSQUARES_API_KEY")
if not API_KEY:
    raise RuntimeError("API key is missing. Please check your .env file.")
