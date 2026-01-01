from pydantic import BaseModel
from typing import List


class CareerRequest(BaseModel):
    message: str


class CareerResponse(BaseModel):
    career_options: List[str]
    required_skills: List[str]
    learning_path: str
    career_advice: str


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str
