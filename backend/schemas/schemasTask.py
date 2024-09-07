from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime 
    status: Optional[str] = Field('em aberto', regex='^(concluída|em aberto|em andamento)$')
    user_id: Optional[int] = None


class TaskResponse(TaskCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
