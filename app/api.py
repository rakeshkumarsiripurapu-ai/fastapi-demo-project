from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"users": ["Alice", "Bob"]}

@router.post("/users")
def create_user(user: dict):
    return {"message": "User created", "user": user}
