from fastapi import FastAPI

from backend.routers import users_routers, admin_user_routers, task_routers
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost:3000",  # Adicione a origem do seu front-end
]
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Você pode especificar os domínios permitidos aqui
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")  
async def root():
    return {"mensagem": "todo app is running"}

app.include_router(admin_user_routers.router, prefix="/api/v1")
app.include_router(users_routers.router, prefix="/api/v1")
app.include_router(task_routers.router, prefix="/api/v1")


# Outras rotas e configurações do FastAPI podem ser adicionadas aqui
