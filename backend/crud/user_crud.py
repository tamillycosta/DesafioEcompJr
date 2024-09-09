from backend.database.database  import Database
from backend.database.database import Database
from abc import abstractmethod
from typing import Optional



         
class UserCrud:
    def __init__(self):
        self.db = Database()
         
    def login(self, username: str, password: str) -> bool:
        
        cursor, con = self.db.get_cursor()
        try:
            query = 'SELECT * FROM users WHERE username = ? AND password = ? '
            params = (username,password)
            
            cursor.execute(query, params)
            user = cursor.fetchone()
            
            if user:
                    return True
            
            return False
         
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return False  # Retorna False em caso de erro
            
        finally:
            con.close()

            
    @abstractmethod       
    def cadastrar_conta():
            pass
  
            

        

