from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from backend.database.database import Task  
from typing import Optional, List


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db
   
    def create_task(self, task: Task) -> Optional[Task]:
        try:
            self.db.add(task)
            self.db.commit()
            return task  
        except IntegrityError as e:
            self.db.rollback()
            print(f"IntegrityError: {e}")  # Para depuração
            return None
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")  # Para depuração
            return None

    
    def delete_task(self, task_id: int) -> None:
        try:
            task = self.db.query(Task).filter(Task.id == task_id).first()
            if task:
                self.db.delete(task)
                self.db.commit()
               
            else:
                return None
        except Exception as e:
            self.db.rollback()
            return e
    
    def get_task_by_name(self, title: str) -> Optional[Task]:
        try:
            return self.db.query(Task).filter(Task.title == title).first()
        except Exception as e:
           
            return e
    
    
    def get_tasks(self) -> List[Task]:
        try:
            return self.db.query(Task).all()
        except Exception as e:
           
            return []
    
    
    def update_task(self, task_id: int, updated_task: Task) -> Optional[Task]:
        try:
            task = self.db.query(Task).filter(Task.id == task_id).first()
            if task:
                task.title = updated_task.title
                task.description = updated_task.description
                task.due_date = updated_task.due_date
                task.status = updated_task.status
                self.db.commit()
                return task  
            else:
                
                return e
        except Exception as e:
            self.db.rollback()
         
            return e
    
    
    
    def update_task_status(self, task_id: int, status: str) -> Optional[Task]:
        try:
            task = self.db.query(Task).filter(Task.id == task_id).first()
            if task:
                valid_statuses = ['concluída', 'em aberto', 'em andamento']
                if status not in valid_statuses:
                    raise ValueError("Status inválido.")
                
                task.status = status
                self.db.commit()
                return task  
            else:
              
                return None
        except Exception as e:
            self.db.rollback()
           
            return e
