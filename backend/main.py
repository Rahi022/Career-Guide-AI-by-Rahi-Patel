from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import CareerRequest
from ai_client import get_ai_response
from database import SessionLocal, History
from user_routes import router as user_router
from resume import router as resume_router

app = FastAPI(title="CareerGuide AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(user_router)
app.include_router(resume_router)


@app.post("/career")
def career_guide(request: CareerRequest):
    result = get_ai_response(request.message)

    db = SessionLocal()
    record = History(
        user="demo",
        query=request.message,
        response=str(result)
    )
    db.add(record)
    db.commit()

    return result
