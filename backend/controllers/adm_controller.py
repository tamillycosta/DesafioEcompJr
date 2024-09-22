from backend.models.adm_models import Adm
from backend.models.user_model import  User
from backend.service.adm_service import AdmService
from backend.service.user_service import UserService
from sqlalchemy.orm import Session

class AdmController:
    def __init__(self, db: Session ) -> None:
        self.adm_service = AdmService(db)
        self.user_service = UserService(db)
    
    def login(self,username: str, password: str) -> bool:
        adm = self.adm_service.get_adm(username)
        if adm and adm.password == password:
            return adm
    
    def create_adm_account(self, adm: Adm):
        self.adm_service.create_user(adm)

    
    def create_user(self,user: User):
        self.user_service.register_user(user)
        
    def update_user(self, id:int, user : User):
        self.user_service.update_user_info(id, user)
        
    def get_users(self) -> list[User]:
        return self.user_service.get_users()
        
    def get_user (self, username : str) -> User:
       return self.user_service.get_user(username)
   
    def delete_user(self, id: int) -> None:
       self.user_service.delete_user(id)
        