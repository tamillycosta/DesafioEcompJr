from fastapi import FastAPI
from backend.database.database import Database, TableCreator
from backend.routers import user_routers
app = FastAPI()


database = Database()
table_creator = TableCreator(database)
table_creator.create_tables()



@app.get("/")  
async def root():
    return {"mensagem": "todo app is running"}

app.include_router(user_routers.router, prefix="/api/v1")


# Outras rotas e configurações do FastAPI podem ser adicionadas aqui
