from fastapi import APIRouter
from models import UserCreate, UserLogin
from auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth")

users = []


@router.post("/signup")
def signup(user: UserCreate):
    users.append({
        "email": user.email,
        "password": hash_password(user.password)
    })
    return {"message": "User created"}


@router.post("/login")
def login(user: UserLogin):
    for u in users:
        if u["email"] == user.email and verify_password(user.password, u["password"]):
            token = create_access_token({"sub": user.email})
            return {"access_token": token}

    return {"error": "Invalid credentials"}
