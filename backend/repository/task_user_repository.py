from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from backend.database.database import User, Task, task_users_table
from backend.models.tasks_model import TaskUser  


class TaskUserRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_tasks_from_user(self, user_id: int) -> list:
        try:
            tasks = self.db.query(Task).filter(Task.user_id == user_id).all()
            return tasks
        
        except SQLAlchemyError as e:
            self.db.rollback()  
            print(f"Error: {e}")
            return []
