from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import hello, auth  # Import the auth router
from app.exceptions import add_exception_handlers

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

add_exception_handlers(app)  # Add global exception handler

# Include routers
app.include_router(hello.router, tags=["Hello"])  # Include the "hello" router
app.include_router(auth.router, tags=["Authentication"])  # Include the "auth" router

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Agreement Repository API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
