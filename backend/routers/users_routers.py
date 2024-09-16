from fastapi import APIRouter, HTTPException
from backend.models.user_model import User
from backend.models.tasks_model import TaskUser
from backend.controllers.user_controller import UserController


router = APIRouter()
user_controller = UserController()

@router.post("/login")
async def login(username: str, password: str):
    user = user_controller.login(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@router.post("/register")
async def register_account(user: User):
    try:
        user_controller.register_account(user)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete_account/{user_id}")
async def delete_account(user_id: int):
    try:
        user_controller.delete_account(user_id)
        
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/add-user-task")
async def add_task(task_user: TaskUser):
    try:
        user_controller.add_task(task_user)
       
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete-user-task")
async def delete_task(task_id: int, user_id: int):
    try:
        user_controller.delete_task(task_id, user_id)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/get-user-tasks/{user_id}")
async def get_tasks(user_id: int):
    try:
        tasks = user_controller.get_tasks(user_id)
        return {"tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
