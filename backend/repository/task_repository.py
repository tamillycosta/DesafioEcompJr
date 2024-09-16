from backend.database.database  import Database
from backend.models.tasks_model import Task
import sqlite3
from typing import Optional, List


class TaskRepository:
    def __init__(self) -> None:
        self.db = Database()
        
        
    def create_task(self,task: Task):
        
        cursor, con = self.db.get_cursor()
        try:
            cursor.execute(
                '''INSERT INTO tasks (title, description, created_at, due_date, status ) 
                   VALUES (?, ?, ?, ?, ? )
                ''',  (task.title, task.description, task.create_at, task.due_date, task.status)
            )
            con.commit()
            return cursor.lastrowid  
        
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao criar tarefa: {e}")
        except Exception as e:
            print(f"Erro ao criar tarefa: {e}")
        finally:    
            cursor.close() 
            self.db.close_connection(con)
            
            
        
    def delete_task(self, id: int):
        cursor, con = self.db.get_cursor()
        
        try:
            cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
            con.commit()
            
            if cursor.rowcount > 0:
                 print("deletado")
            else:
                print("task nao existe")
                
        except Exception as e :
            print(f"Erro ao deletar task: {e}")
        finally:
            cursor.close()
            self.db.close_connection(con)
            
            
            
    def get_task_byname(self, title: str):
        cursor, conn = self.db.get_cursor()
        cursor.execute('SELECT * FROM tasks WHERE title = ?', (title,))
        task = cursor.fetchone()
        
        if not task:
            return None
        
        # Transformar a tupla em um dicionário com os nomes corretos
        task_dict = {
            "id": task["id"],
            "title": task["title"],
            "description": task["description"],
            "created_at": task["created_at"],  # Ajustar para o nome correto
            "due_date": task["due_date"],
            "status": task["status"]
        }
        self.db.close_connection(conn)
        return task_dict

     
     
    def get_tasks(self)-> List[Task]:
        cursor, con = self.db.get_cursor()
        
        try:
            cursor.execute('SELECT * FROM tasks')
            tasks = cursor.fetchone()
        except Exception as e:
            print(f"Erro as tarefas: {e}")
        finally:
            self.db.close_connection(con)
            return tasks

        
          
    def update_tasks(self, id, task: Task):
        cursor, con = self.db.get_cursor()
        try:
            # Debug print para verificar os valores que estão sendo passados
            print(f"Atualizando tarefa {id} com status: {task.status}")
            
            cursor.execute('''
                UPDATE tasks
                SET title = ?, description = ?, due_date = ?, status = ?
                WHERE id = ?
            ''', (task.title, task.description, task.due_date, task.status, id))
            
            con.commit()
        except Exception as e:
            print(f"Erro ao editar tarefas: {e}")
        finally:
            self.db.close_connection(con)
            
            
            
    def update_task_status(self, task_id: int, status: str):
        cursor, conn = self.db.get_cursor()
        try:
            # Verifica se o status é válido
            valid_statuses = ['concluída', 'em aberto', 'em andamento']
            if status not in valid_statuses:
                raise ValueError("Status inválido")
            
            # Atualiza o status da tarefa
            cursor.execute('''
                UPDATE tasks
                SET status = ?
                WHERE id = ?
            ''', (status, task_id))
            
            conn.commit()
            if cursor.rowcount == 0:
                raise ValueError("Tarefa não encontrada")
            
        except sqlite3.Error as e:
            return {"error": f"Erro ao atualizar o status: {e}"}
        except ValueError as e:
            return {"error": str(e)}
        finally:
            self.db.close_connection(conn)

   
    
            
    
        