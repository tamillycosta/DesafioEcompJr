from backend.crud.user_crud import UserCrud
import sqlite3


class RegularUserCrud(UserCrud):
    def __init__(self):
        super().__init__()
        
    def cadastrar_conta(self, username, password, email):
    
        cursor, con = self.db.get_cursor()
        self.is_admin =  False
        try:
            cursor.execute('''
                INSERT INTO users (username, password, email, is_admin) 
                VALUES (?, ?, ?, ?, )
            ''', (username, password, email, self.is_admin))
            
            con.commit()  
            print("Conta criada com sucesso.")
            return cursor.lastrowid  
        
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao criar usuário: {e}")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(con)