from fastapi import FastAPI
from .routers import auth, tasks
from .database import engine, Base

# Create tables (for development, but migrations should be used)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", version="1.0.0")

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager API. Go to /docs for documentation."}