from backend.models.user_model import User
from backend.database.database import Database
from typing import Optional, List
import sqlite3

class UserRepository:
    
    def __init__(self):
        self.db = Database()


    def create_user(self, user: User) -> None:
       
        cursor, conn = self.db.get_cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, password, email)
                VALUES (?, ?, ?)
            ''', (user.username, user.password, user.email))
            conn.commit()
     
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao criar usuário: {e}")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(conn)


    def get_user(self, username: str) -> Optional[User]:
        
        cursor, conn = self.db.get_cursor()
        try:
            cursor.execute('''
                SELECT * FROM users WHERE username = ?
            ''', (username,))
            row = cursor.fetchone()
            if row:
                return User(username=row['username'], password=row['password'], email=row['email'])
            return None
    
        except Exception as e:
            print(f"ERRO AO BUSCAR USER: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(conn)


    def get_all_users(self) -> List[User]:
       
        cursor, conn = self.db.get_cursor()
        try:
            cursor.execute('SELECT * FROM users')
            rows = cursor.fetchall()
        
        except Exception as e:
            print(f"Erro ao listar usuário: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(conn)
            return [User(username=row['username'], password=row['password'], email=row['email']) for row in rows]


    def update_user(self, id: int, user: User) -> None:
        
        cursor, conn = self.db.get_cursor()
        try:
            cursor.execute('''
                UPDATE users
                SET password = ?, email = ?
                WHERE id = ?
            ''', (user.password, user.email, id))
            conn.commit()
        except Exception as e:
            print(f"Erro ao editar usuário: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(conn)
        
        

    def delete_user(self, id: int) -> None:
      
        cursor, conn = self.db.get_cursor()
        try:
            cursor.execute('''
                DELETE FROM users WHERE id = ?
            ''', (id,))
            conn.commit()
        except Exception as e:
            print(f"Erro ao editar usuário: {e}")
        finally:
            cursor.close() 
            self.db.close_connection(conn)
        
       

