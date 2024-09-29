from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from  backend.database.database import User

from typing import Optional, List




class UserRepository:
    
    def __init__(self, db: Session):
        self.db = db


    def create_user(self, user: User) -> None:
        try:
            self.db.add(user)
            self.db.commit()
        except IntegrityError as e:
            self.db.rollback() 
            return e
        except Exception as e:
            self.db.rollback()
            return e

    def get_user(self, username: str) -> Optional[User]:
        try:
            return self.db.query(User).filter(User.username == username).first()  
        except Exception as e:
         
            return e
        
    def get_all_users(self) -> List[User]:
        try:
            return self.db.query(User).all()  
        except Exception as e:
         
            return []
        
    def update_user(self, id: int, user: User) -> None:
        try:
            existing_user = self.db.query(User).filter(User.id == id).first()  
            if existing_user:
                existing_user.username = user.username
                existing_user.password = user.password 
                existing_user.email = user.email
                self.db.commit()
            else:
               return None 
        except Exception as e:
            self.db.rollback() 
            return e
           
    
    def delete_user(self, id: int) -> None:
        try:
            user = self.db.query(User).filter(User.id == id).first() 
            if user:
                self.db.delete(user)  
                self.db.commit()
            else:
               return None
        except Exception as e:
            self.db.rollback()  
            return e

  

    def get_user(self, username: str) -> Optional[User]:
        print(f"Buscando usuário: {username}")
        user = self.db.query(User).filter(User.username == username).first()
        print(f"Resultado da busca: {user}")
        return user

        
        
        
    def get_all_users(self) -> List[User]:
        try:
            return self.db.query(User).all()  # Busca todos os usuários
        except Exception as e:
         
            return []
        
    def update_user(self, id: int, user: User) -> None:
        try:
            existing_user = self.db.query(User).filter(User.id == id).first()  
            if existing_user:
                existing_user.username = user.username
                existing_user.password = user.password 
                existing_user.email = user.email
                self.db.commit()
            else:
               return None 
        except Exception as e:
            self.db.rollback() 
           
    
    def delete_user(self, id: int) -> None:
        try:
            user = self.db.query(User).filter(User.id == id).first() 
            if user:
                self.db.delete(user)  
                self.db.commit()
            else:
               return None
        except Exception as e:
            self.db.rollback()  
