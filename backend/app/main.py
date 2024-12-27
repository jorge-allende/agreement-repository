import os
import json
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from app.routers.linksquares import router as linksquares_router
from app.routers.auth import router as auth_router  # Import the auth router
from config import API_KEY  # Centralized configuration for API keys and environment variables

# Ensure API key is loaded
if not API_KEY:
    raise RuntimeError("API key is missing. Please check your .env file.")

# Load the custom OpenAPI JSON
def custom_openapi():
    try:
        with open("backend/static/openapi.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise RuntimeError("OpenAPI JSON file not found. Ensure 'backend/static/openapi.json' exists.")

app = FastAPI()

# Set custom OpenAPI schema
app.openapi = custom_openapi

# Use the absolute path to serve static files
static_dir = os.path.join(os.path.dirname(__file__), "../static")
if not os.path.exists(static_dir):
    raise RuntimeError(f"Static directory not found: {static_dir}")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(linksquares_router, prefix="/analyze/v1", tags=["LinkSquares"])
app.include_router(auth_router, prefix="", tags=["Authentication"])  # Add the auth router

# Add a custom Swagger UI endpoint
@app.get("/api-testing", include_in_schema=False)
async def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/static/openapi.json",  # Path to your OpenAPI JSON file
        title="API Testing",
    )

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Agreement Repository API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
