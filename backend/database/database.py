from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, ForeignKey, CheckConstraint, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session


Base = declarative_base()

# Definição das classes para os modelos
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    tasks = relationship("Task", back_populates="user")

class Adm(Base):
    __tablename__ = 'adm'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(String)
    due_date = Column(String)
    status = Column(String, CheckConstraint("status IN ('concluída', 'em aberto', 'em andamento')"))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="tasks")

# Tabela associativa para tarefas e usuários
task_users_table = Table(
    'task_users', Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id', ondelete='CASCADE'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
)

# Configuração do banco de dados
class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self):
        """Cria todas as tabelas no banco de dados."""
        Base.metadata.create_all(self.engine)

    def drop_tables(self):
        """Remove todas as tabelas (útil para testes)."""
        Base.metadata.drop_all(self.engine)

    def get_session(self):
        """Obtém uma sessão do banco de dados."""
        return self.SessionLocal()




db_url = "sqlite:///./database.db" 
database = Database(db_url)
database.create_tables()

def get_db():
    db = database.SessionLocal()
    print("New database session created.")
    try:
        yield db
    finally:
        db.close()
        
        
