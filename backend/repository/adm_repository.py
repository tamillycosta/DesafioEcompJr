from backend.database.database import Adm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError



class AdmRepository():
    
    def __init__(self, db: Session):
        self.db = db
             
    def create_user(self, adm: Adm):
        
        try:
            self.db.add(adm)
            self.db.commit()
        except IntegrityError as e:
            self.db.rollback() 
        except Exception as e:
            self.db.rollback()


    def delete_user(self, id : int )-> None:
        try:
            user = self.db.query(Adm).filter(Adm.id == id).first() 
            if user:
                self.db.delete(user)  
                self.db.commit()
            else:
               return None
        except Exception as e:
            self.db.rollback()  


    def get_user(self, username: str):
        try:
            return self.db.query(Adm).filter(Adm.username == username).first()
        except Exception as e:
           return None
        

            


        