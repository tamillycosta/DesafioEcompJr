from backend.repository.adm_repository import AdmRepository
from backend.models.adm_models import Adm


class AdmService:
    def __init__(self) -> None:
        self.adm_repo = AdmRepository()
        
    def create_user(self, adm: Adm) -> None:
        self.adm_repo.create_user(adm)
        
        
    def delete(self, id: int) -> None:
        self.adm_repo.delete_user(id)
        
    def get_adm(self, name: str):
        return self.adm_repo.get_user(name)
    