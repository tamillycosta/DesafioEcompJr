
from backend.models.tasks_model import TaskUser
from backend.repository.task_user_repository import TaskUserRepository


class TaskUserService:
    
    def __init__(self) -> None:
        self.task_user_repo = TaskUserRepository()
        
    def add_user_task(self, task: TaskUser):
        self.task_user_repo.assing_task_to_user(task)
        
    def delete_user_task(self, task: TaskUser):
         self.task_user_repo.remove_task_from_user(task)
         
    def list_user_tasks(self, user_id: int):
       return self.task_user_repo.list_tasks_from_user(user_id)
        
    