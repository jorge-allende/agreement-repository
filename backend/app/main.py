from fastapi import FastAPI
from routers import hello
from app.exceptions import add_exception_handlers

app = FastAPI()

add_exception_handlers(app)  # Add global exception handler

app.include_router(hello.router)  # Include the "hello" router

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Agreement Repository API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
