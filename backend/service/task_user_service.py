
from backend.models.tasks_model import TaskUser
from sqlalchemy.orm import Session
from backend.repository.task_user_repository import TaskUserRepository


class TaskUserService:
    
    def __init__(self,db: Session) -> None:
        self.task_user_repo = TaskUserRepository(db)
         
    def list_user_tasks(self, user_id: int):
       return self.task_user_repo.list_tasks_from_user(user_id)
        
    