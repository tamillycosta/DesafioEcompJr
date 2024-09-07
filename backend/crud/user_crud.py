from backend.database.database  import Database
import sqlite3
from backend.database.database import Database


class UserCrud:
    def __init__(self):
        self.db = Database()
        
    

    
class AdminUserCrud(UserCrud):
    def __init__(self):
        super().__init__()
        
    
    def create_user(self, username : str, password: str, email:str, is_admin:bool=False):
    
        cursor, con = self.db.get_cursor()

        try:
            cursor.execute('''
                INSERT INTO users (username, password, email, is_admin) 
                VALUES (?, ?, ?, ?)
            ''', (username, password, email, is_admin))
            
            con.commit()  
            print("Usuário criado com sucesso.")
            return cursor.lastrowid  

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao criar usuário: {e}")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(con)



    def delete_user(self, user_id : int ):
        cursor, con = self.db.get_cursor()
        try:
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            
            con.commit()
            if cursor.rowcount > 0:
                print("deletado")
            else:
                print("id nao encontrado")
                
        except Exception as e :
            print(f"Erro ao deletar usuário: {e}")
        finally:
            cursor.close()
            self.db.close_connection(con)

        
    def get_user(self, user_id: int):
         cursor, con = self.db.get_cursor()
         try:
             cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
             user = cursor.fetchone()
             return user if user else None
         
         except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            
         finally:
            cursor.close()
            self.db.close_connection(con)
            
            
    def list_users(self):
        cursor, con = self.db.get_cursor()
        try:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            return users
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
        finally:
            self.db.close_connection(con)
            
        
        




