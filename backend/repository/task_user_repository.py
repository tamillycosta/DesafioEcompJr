
from backend.database.database import Database
from backend.models.tasks_model import TaskUser
import sqlite3


class TaskUserRepository:
    def __init__ (self):
        self.database = Database()
        
    def assing_task_to_user(self,task_user:TaskUser):
        """
        Associa uma tarefa existente a um usuário.
        
        Args:
            task_id (int): ID da tarefa a ser associada.
            user_id (int): ID do usuário que será associado à tarefa.
        """
        cursor, conn = self.database.get_cursor()
        
        try:
            cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_user.task_id,))
            task = cursor.fetchone()

            cursor.execute('SELECT * FROM users WHERE id = ?', (task_user.user_id,))
            user = cursor.fetchone()

            if not user or not task : return None
            
            cursor.execute('SELECT * FROM task_users WHERE task_id = ? AND user_id = ?', (task_user.task_id, task_user.user_id))
            existing_assignment = cursor.fetchone()
            
            if existing_assignment: return None
            
            # Insere o relacionamento na tabela task_users
            cursor.execute('''
                INSERT INTO task_users (task_id, user_id)
                VALUES (?, ?)
            ''', (task_user.task_id, task_user.user_id))
            
            conn.commit()
               
        except sqlite3.Error as e:
            return {"error": f"Erro ao associar a tarefa: {e}"}
        
        finally:
            self.database.close_connection(conn)
            
            
            
    def remove_task_from_user(self, task_user:TaskUser):
        """
        Remove a associação de uma tarefa de um usuário.
        
        Args:
            task_id (int): ID da tarefa.
            user_id (int): ID do usuário.
        
        Returns:
            dict: Resultado da operação (sucesso ou erro).
        """
        
        cursor, conn = self.database.get_cursor()
        
        try:
            cursor.execute('SELECT * FROM task_users WHERE task_id = ? AND user_id = ?', (task_user.task_id, task_user.user_id))
            association = cursor.fetchone()
            
            if not association:
                return {"error": f"A tarefa {task_user.task_id} não está associada ao usuário {task_user.user_id}."}
            
            cursor.execute('DELETE FROM taks_users WHERE task_id = ? AND user_id = ?', (task_user.task_id, task_user.user_id))
            conn.commit()
            
            return {"success": f"Tarefa {task_user.task_id} removida do usuário {task_user.user_id} com sucesso."}
        
        except sqlite3.Error as e:
            return {"error": f"Erro ao remover a associação: {e}"}
        
        finally:
            self.database.close_connection(conn)
            
            
            
            
    def list_tasks_from_user(self, user_id: int):
        """
        Lista todas as tarefas associadas a um usuário.
        
        Args:
            user_id (int): ID do usuário para o qual listar as tarefas.
            
        Returns:
            list: Lista de tarefas associadas ao usuário.
        """
        cursor, conn = self.database.get_cursor()
        
        
        try:
            # Usando um JOIN para combinar as tabelas task_users e tasks
            cursor.execute('''
                SELECT tasks.id, tasks.title, tasks.description, tasks.status, tasks.due_date
                FROM task_users
                JOIN tasks ON task_users.task_id = tasks.id
                WHERE task_users.user_id = ?
            ''', (user_id,))
            
        
            tasks = cursor.fetchall()
            
            if not tasks:
                return {"message": f"Nenhuma tarefa encontrada para o usuário {user_id}."}
            
            # Transformar os resultados em uma lista de dicionários
            tasks_list = []
            for task in tasks:
                tasks_list.append({
                    "id": task["id"],
                    "title": task["title"],
                    "description": task["description"],
                    "status": task["status"],
                    "due_date": task["due_date"]
                })
            
            return tasks_list
        
        except sqlite3.Error as e:
            return {"error": f"Erro ao listar tarefas: {e}"}
        
        finally:
            self.database.close_connection(conn)

            