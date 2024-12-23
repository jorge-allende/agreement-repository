from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routers import hello, auth, linksquares  # Import the auth router
from app.exceptions import add_exception_handlers

app = FastAPI()

# Serve static files (e.g., openapi.json)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Add exception handlers
add_exception_handlers(app)

# Include routers
app.include_router(hello.router, tags=["Hello"])  # Include the "hello" router
app.include_router(auth.router, tags=["Authentication"])  # Include the "auth" router
app.include_router(linksquares.router, tags=["LinkSquares"])  # Include the "linksquares" router

# Serve the openapi.json directly as a JSON response
@app.get("/openapi.json", tags=["API Docs"])
async def get_openapi_json():
    """
    Serve the OpenAPI JSON file for RapiDoc.
    """
    try:
        with open("static/openapi.json", "r") as f:
            return f.read()
    except FileNotFoundError:
        return {"error": "openapi.json file not found"}

@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Agreement Repository API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
