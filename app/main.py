from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, tasks # Import your new router modules

# Spin up database tables on app startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PrimeTrade Task Management Engine")

# Unlock global access via CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect the routers like modular building blocks
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"status": "Online", "documentation": "/docs"}