from fastapi import FastAPI
from backend.database.database import Database, TableCreator
from backend.routers import admin_user_routers, users_routers
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


database = Database()
table_creator = TableCreator(database)
table_creator.create_tables()



# Adiciona o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")  
async def root():
    return {"mensagem": "todo app is running"}

app.include_router(admin_user_routers.router, prefix="/api/v1")
app.include_router(users_routers.router, prefix="/api/v1")

# Outras rotas e configurações do FastAPI podem ser adicionadas aqui
