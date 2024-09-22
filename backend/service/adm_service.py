from backend.repository.adm_repository import AdmRepository
from backend.models.adm_models import Adm
from backend.database.database import Adm as AdmTable
from sqlalchemy.orm import Session
from sqlalchemy.exc import  SQLAlchemyError


class AdmService:
    def __init__(self, db: Session) -> None:
        self.adm_repo = AdmRepository(db)
        
        
    def create_user(self, user: Adm) -> None:
        try:
            db_adm = AdmTable(  
                username=user.username,
                password=user.password,
                email=user.email
            )
            self.adm_repo.create_user(db_adm)
        except Exception as e:
            print(f"Error registering user: {e}") 
        
        
    def delete(self, id: int) -> None:
        
        try:
            adm = self.adm_repo.delete_user(id)
            if not adm:
                raise ValueError(f"Usuário com id '{id}' não encontrado.")
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao remover o usuário: {str(e)}")
        
        
        
    def get_adm(self, name: str):
        return self.adm_repo.get_user(name)
    