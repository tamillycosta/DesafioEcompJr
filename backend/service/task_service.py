from backend.repository.task_repository import TaskRepository
from backend.models.tasks_model import Task


class TaskService:
    
    def __init__(self) -> None:
        self.task_repo = TaskRepository()
        
    def create_task(self,task:Task):
        self.task_repo.create_task(task)
        
    def delete_task(self, id: int):
        self.task_repo.delete_task(id)
        
    def update_task_status(self,id: int, status: str):
        self.task_repo.update_task_status(id, status)
        
    def update_task(self,id: int, task:Task):
        self.task_repo.update_tasks(id, task)
        
    def get_tasks(self):
        return self.task_repo.get_tasks()
    
    def get_task(self, title : str):
        return self.task_repo.get_task_byname(title)
    
    