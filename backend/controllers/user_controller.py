from backend.models.user_model import User
from backend.models.tasks_model import TaskUser
from backend.service.user_service import UserService
from  backend.service.task_user_service import TaskUserService
from sqlalchemy.orm import Session

class UserController:
    
    def __init__(self,db: Session ) -> None:
        self.user_service = UserService(db)
        self.manager_service = TaskUserService(db)
        
    def login(self,username: str, password: str) -> User:
        user = self.user_service.get_user(username)
        if user and user.password == password:
            return user
        else:
            return None
    
    def register_account(self, user: User):
        self.user_service.register_user(user)
        
    def delete_account(self, id:int):
         self.user_service.delete_user(id)
         
        
    def get_tasks(self, user_id:int):
        return self.manager_service.list_user_tasks(user_id)
    
    
        

            
            