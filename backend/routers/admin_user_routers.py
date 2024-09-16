from fastapi import APIRouter, HTTPException
from backend.controllers.adm_controller import AdmController
from backend.models.adm_models import Adm
from backend.models.user_model import User


admin_controller =  AdmController()
router = APIRouter()


@router.post("/adm/create-account")   
async def create_account_router(adm: Adm):
    try:
        admin_controller.create_adm_account(adm)
    except  Exception as e:
        raise HTTPException(status_code= 400, detail=str(e))


@router.post("/login-adm")
async def login(username: str, password: str):
    adm = admin_controller.login(username, password)
    if not adm:
        raise HTTPException(status_code=401, detail="Invalid username or password")  
    else:
        return adm
    
    
@router.post("/adm/create-user", status_code=204)
async def create_user_router(user: User):
    try:
       admin_controller.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {e}")


@router.delete("/adm/delete-user")
async def delete_user_router(id: int):
    try:
        admin_controller.delete_user(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar usuário: {e}")


@router.put("/adm/edit-user")
async def uptdate_user_router(id: int, user: User):
    try:
        admin_controller.update_user(id, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao editar usuário: {e}")


@router.get("/adm-get/{username}")
async def get_user_route(username: str):
    user = admin_controller.get_user(username)
    if user:
        return user
    else:
        raise HTTPException(status_code= 404, detail="usuário não encontrado")
    
    
@router.get("/adm-list-users", status_code=200)
def list_users_route():
    try:
        users = admin_controller.get_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {e}")
    