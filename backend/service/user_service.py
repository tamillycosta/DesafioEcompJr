
from sqlalchemy.orm import Session
from backend.repository.user_repository import UserRepository
from backend.models.user_model import User
from backend.database.database import User as slqUser
from sqlalchemy.exc import NoResultFound, SQLAlchemyError


class UserService:
    def __init__(self, db: Session ) -> None:
        self.user_repo = UserRepository(db)
        self.db_user = slqUser()
        
        
    def register_user(self, user: User) -> None:
        try:
            existing_user = self.user_repo.get_user(user.username)
            if existing_user:
                raise ValueError("Username already exists")
            
            db_user = slqUser(  # Use o modelo SQLAlchemy
                username=user.username,
                password=user.password,
                email=user.email
            )
            self.user_repo.create_user(db_user)
        except Exception as e:
            print(f"Error registering user: {e}") 
            
            

    def update_user_info(self, id: int, user: User):
       
        try:
            self.db_user.username = user.username
            self.db_user.password = user.password  
            self.db_user.email = user.email
            
            self.user_repo.update_user(id,self.db_user)
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao atualizar o usuário: {str(e)}")
        
                  

    def get_users(self) -> list[User]:
      
        try:
            users = self.user_repo.get_all_users()
            return users if users else []
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao buscar usuários: {str(e)}")
       
       
       
    def get_user(self, username: str) -> User:
        
        try:
            user = self.user_repo.get_user(username)
            if not user:
                raise ValueError(f"Usuário '{username}' não encontrado.")
            return user

        except NoResultFound:
            raise ValueError(f"Usuário '{username}' não encontrado.")
        
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao buscar o usuário: {str(e)}")
   
   
   
    def delete_user(self, id: int) -> dict:
       
        try:
            user = self.user_repo.delete_user(id)
            return {"success": f"Usuário '{id}' removido com sucesso."}

        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao remover o usuário: {str(e)}")
