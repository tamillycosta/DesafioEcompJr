from fastapi import APIRouter, HTTPException, Depends
from backend.controllers.adm_controller import AdmController
from backend.models.adm_models import Adm
from backend.models.user_model import User
from sqlalchemy.orm import Session
from  backend.database.database import get_db


router = APIRouter()


@router.post("/adm/create-account")   
async def create_account_router(adm: Adm, db: Session = Depends(get_db)):
    admin_controller =  AdmController(db)
    try:
        admin_controller.create_adm_account(adm)
    except  Exception as e:
        raise HTTPException(status_code= 400, detail=str(e))
    return {"success": True}


@router.post("/login-adm")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    admin_controller =  AdmController(db)
    adm = admin_controller.login(username, password)
    if not adm:
        raise HTTPException(status_code=401, detail="Invalid username or password")  
    else:
        return {"success": True}
    
    
    
@router.post("/adm/create-user", status_code=204)
async def create_user_router(user: User, db: Session = Depends(get_db)):
    admin_controller =  AdmController(db)
    try:
       admin_controller.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {e}")
    return {"success": True}


@router.delete("/adm/delete-user{id}")
async def delete_user_router(id: int, db: Session = Depends(get_db)):
    admin_controller =  AdmController(db)
    try:
        admin_controller.delete_user(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar usuário: {e}")
    return {"success": True}


@router.put("/adm/edit-user/{id}")
async def uptdate_user_router(id: int, user: User, db: Session = Depends(get_db)):
    admin_controller =  AdmController(db)
    try:
        admin_controller.update_user(id, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao editar usuário: {e}")
    return {"success": True}


@router.get("/adm-get/{username}")
async def get_user_route(username: str, db: Session = Depends(get_db)):
    admin_controller =  AdmController(db)
    user = admin_controller.get_user(username)
    if user:
        return user
    else:
        raise HTTPException(status_code= 404, detail="usuário não encontrado")
    
    
@router.get("/adm-list-users", status_code=200)
def list_users_route(db: Session = Depends(get_db)):
    admin_controller =  AdmController(db)
    try:
        users = admin_controller.get_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {e}")
    