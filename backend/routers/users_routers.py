from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models.user_model import User
from backend.models.tasks_model import TaskUser
from backend.controllers.user_controller import UserController
from  backend.database.database import get_db


router = APIRouter()


@router.post("/login")
async def login(credentials: dict, db: Session = Depends(get_db)):
    username = credentials.get("username")
    password = credentials.get("password")
    
    user_controller = UserController(db)
    user = user_controller.login(username, password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    return  user



@router.post("/register")
async def register_account(user: User, db: Session = Depends(get_db)):
    user_controller = UserController(db)
    try:
        user_controller.register_account(user)
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/delete_account/{user_id}", )
async def delete_account(user_id: int, db: Session = Depends(get_db)):
    user_controller = UserController(db)
    try:
        user_controller.delete_account(user_id)
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.get("/get-user-tasks/{user_id}")
async def get_tasks(user_id: int, db: Session = Depends(get_db)):
    user_controller = UserController(db)
    try:
        tasks = user_controller.get_tasks(user_id)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
