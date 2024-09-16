import sqlite3


class Database():
    
    def __init__(self):
        self.db_name = 'database.db'
        
    def get_connection(self):  
        try:
            connection = sqlite3.connect(self.db_name)
            connection.row_factory = sqlite3.Row
            return connection
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
    
    def get_cursor(self):
        conn = self.get_connection()
        if conn:
            return conn.cursor(), conn
        else:
            return None, None
    
    def close_connection(self, connection):
        if connection:
            connection.commit()
            connection.close()

        
    
    
class TableCreator():
    
    def __init__(self,database: Database) -> None:
        self.database = database
        
     
    def create_regular_users_table(self):
        """Cria a tabela de usuários no banco de dados se não existir."""
        cursor, conn = self.database.get_cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
        conn.commit()
        self.database.close_connection(conn)
        
        
    def create_adm_users_table(self):
        """Cria a tabela de usuários no banco de dados se não existir."""
        cursor, conn = self.database.get_cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS adm (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        conn.commit()
        self.database.close_connection(conn)
        
    
    def create_tasks_table(self):
     
        cursor, conn = self.database.get_cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                due_date TIMESTAMP,
                status TEXT CHECK(status  IN ('concluída', 'em aberto', 'em andamento')),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.database.close_connection(conn)

 
       
    def create_task_users_table(self):
        conn = self.database.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS task_users (
                task_id INTEGER,
                user_id INTEGER,
                FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
                PRIMARY KEY (task_id, user_id)
            )
        ''')
        self.database.close_connection(conn)



    def create_tables(self):
        """Cria todas as tabelas no banco de dados se não existirem."""
        self.create_regular_users_table()
        self.create_adm_users_table()
        self.create_tasks_table()
        self.create_task_users_table()
       

    