from fastapi import APIRouter, HTTPException
from backend.models.tasks_model import Task
from backend.controllers.task_controller import  TaskController

router = APIRouter()
task_controller = TaskController()


@router.post("/task-create")
async def create_task_router(task : Task):
    try:
        task_controller.create_task(task)
    except  Exception as e:
        raise HTTPException(status_code= 400, detail=str(e))
    
    
@router.delete("/task-delete")
async def delete_task_router(id: int):
    try:
        task_controller.delete_task(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar tarefa: {e}")
    
    
@router.put("/task-update") 
async def update_task_router(id: int, task:Task):
    try:
         task_controller.update_task(id, task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualiar status da tarefa: {e}")
 
    
@router.put("/uptdate-task-status")
async def uptdate_task_status_router(status: str, task_id: int):
    try:
        task_controller.update_task_status(status, task_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualiar status da tarefa: {e}")
    
    
@router.get("/task-list")
async def get_tasks_router():
    try:
        return task_controller.get_tasks()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar tarefas: {e}")
    
    
@router.get("/task/{title}")
async def get_user_route(title: str):
    task = task_controller.get_task(title)
    if task:
        return task
    else:
        raise HTTPException(status_code= 404, detail="task não encontrada")