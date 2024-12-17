from fastapi import APIRouter

router = APIRouter( prefix="/hero",tags=["hero"])

# Definir rutas para el router
@router.get("/")
async def get_users():
    return [{"id": 1, "name": "Juan"}, {"id": 2, "name": "Ana"}]

@router.get("/hero/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": "Usuario ejemplo"}