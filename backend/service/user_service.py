from backend.repository.user_repository import UserRepository
from backend.models.user_model import User


class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepository()
        
    def register_user(self, user: User):
         
        try:
            self.user_repo.get_user(user.username)
            self.user_repo.create_user(user)
        except:
            raise ValueError 

    def update_user_info(self, id:int, user:User):
        try:
            self.user_repo.update_user(id, user)
        except:
            raise ValueError 
        
    def get_users(self) -> list[User]:
        users = self.user_repo.get_all_users()
        return users if users else None
       
    def get_user (self, username : str) -> User:
       return self.user_repo.get_user(username)
   
    def delete_user(self, id: int) -> None:
       self.user_repo.delete_user(id)
        

    