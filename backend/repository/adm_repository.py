from backend.models.adm_models import Adm
from backend.database.database import Database
import sqlite3
 

# classe responssavel por gerenciar os metodos de um usuário adm no sistema 

class AdmRepository():
    def __init__(self):
        self.db = Database()
             
    def create_user(self, adm: Adm):
        
        cursor, con = self.db.get_cursor()

        try:
            cursor.execute('''
                INSERT INTO adm (username, password, email) 
                VALUES (?, ?, ?)
            ''', (adm.username, adm.password, adm.email ))
            
            con.commit()  
            
            return cursor.lastrowid  

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao criar usuário: {e}")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(con)



    def delete_user(self, user_id : int )-> None:
        cursor, con = self.db.get_cursor()
        try:
            cursor.execute('DELETE FROM adm WHERE id = ?', (user_id,))
            
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


    def get_user(self, username: str):
        
        cursor, conn = self.db.get_cursor()
        try:
            cursor.execute('''
                SELECT * FROM adm WHERE username = ?
            ''', (username,))
            row = cursor.fetchone()
            if row:
                return Adm(username=row['username'], password=row['password'], email=row['email'])
            return None
    
        except Exception as e:
            print(f"ERRO AO BUSCAR USER: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(conn)


        