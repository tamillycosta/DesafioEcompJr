from fastapi import APIRouter, HTTPException
from backend.schemas.schemasUser import UserCreateRequest
from backend.crud.user_adm_crud import AdminUserCrud


admin = AdminUserCrud()
router = APIRouter()


@router.post("/users/create")   
async def create_user_router(user: UserCreateRequest):
    
    try:
        admin.create_user(
            username = user.username,
            password = user.password,
            email = user.email,
        )
        return {"Usuario criado com sucerro"}
    except  Exception as e:
        raise HTTPException(status_code= 400, detail=str(e))
    
    

@router.delete("/users/{user_id}", status_code=204)
async def delete_user_router(user_id: int):
    try:
        admin.delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar usuário: {e}")



@router.get("/users/{user_id}")
async def get_user_route(user_id: int):
    user = admin.get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code= 404, detail="usuário não encontrado")
    
    
@router.get("/users", status_code=200)
def list_users_route():
    try:
        users = admin.list_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {e}")
    