from  backend.service.task_service import TaskService
from backend.models.tasks_model import Task

class TaskController:
    
    def __init__(self) -> None:
        self.task_service = TaskService()
        
    def create_task(self,task:Task):
        self.task_service.create_task(task)
        
    def delete_task(self, id: int):
        self.task_service.delete_task(id)
        
    def update_task(self,id: int, task: Task):
        self.task_service.update_task(id, task)
        
    def update_task_status(self,status:str,task_id : id ):
        self.task_service.update_task_status(task_id,  status)
        
    def get_tasks(self):
        return self.task_service.get_tasks()
    
    def get_task(self, title : str):
        return self.task_service.get_task(title)
    