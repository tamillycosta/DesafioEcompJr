from backend.repository.task_repository import TaskRepository
from backend.models.tasks_model import Task
from sqlalchemy.orm import Session
from backend.database.database import Task as TaskTable
from sqlalchemy.exc import  SQLAlchemyError

class TaskService:
    
    def __init__(self, db: Session) -> None:
        self.task_repo = TaskRepository(db)
        
        
    def create_task(self, task: Task):
        try:
            db_task = TaskTable(
                title=task.title,
                description=task.description,
                created_at= task.create_at,  
                due_date=task.due_date,
                status=task.status,
                user_id  = task.user_id 
            )
            self.task_repo.create_task(db_task)  # Chamada única
        except Exception as e:
            print(f"Error registering task: {e}")
            raise  # Levante o erro para tratamento posterior


            
       
        
    def delete_task(self, id: int):    
        self.task_repo.delete_task(id)
        
        
    def update_task_status(self,id: int, status: str):
        self.task_repo.update_task_status(id, status)
        
        
    def update_task(self,id: int, task:Task):
        try:
            db_task = TaskTable(
                title=task.title,
                description= task.description,
                created_at = task.create_at,
                due_date = task.due_date,
                status = task.status 
            )
            updated_task = self.task_repo.update_task(id, db_task)
            if not updated_task:
                raise ValueError(f"Usuário com id '{id}' não encontrado.")

        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao atualizar o usuário: {str(e)}")
        
        
    def get_tasks(self):
        return self.task_repo.get_tasks()
    
    def get_task(self, title : str):
        return self.task_repo.get_task_by_name(title)
    
    