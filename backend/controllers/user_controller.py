from backend.models.user_model import User
from backend.models.tasks_model import TaskUser
from backend.service.user_service import UserService
from  backend.service.task_user_service import TaskUserService


class UserController:
    
    def __init__(self,) -> None:
        self.user_service = UserService()
        self.manager_service = TaskUserService()
        
    def login(self,username: str, password: str) -> bool:
        user = self.user_service.get_user(username)
        if user and user.password == password:
            return user
    
    def register_account(self, user: User):
        self.user_service.register_user(user)
        
    def delete_account(self, id:int):
         self.user_service.delete_user(id)
         
    def add_task(self, task_user:TaskUser):
        self.manager_service.add_user_task(task_user)
        
    def delete_task(self, task_user:TaskUser):
        self.manager_service.delete_user_task(task_user)
        
    def get_tasks(self, user_id:int):
        return self.manager_service.list_user_tasks(user_id)
    
    
        

            
            