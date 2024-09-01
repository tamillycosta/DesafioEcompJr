from fastapi import FastAPI
from backend.database.database import Database, TableCreator


app = FastAPI()

# Inicialize o banco de dados e crie as tabelas
database = Database()
table_creator = TableCreator(database)
table_creator.create_tables()

@app.get("/")  
async def root():
    return {"mensagem": "Ola fastapi"}

# Outras rotas e configurações do FastAPI podem ser adicionadas aqui
