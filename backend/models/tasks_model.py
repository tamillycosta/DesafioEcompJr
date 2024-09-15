from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    create_at: datetime
    due_date: datetime 
    status: Optional[str] = Field('em aberto', pattern='^(concluída|em aberto|em andamento)$')

    
class TaskUser(BaseModel):
    task_id: int
    user_id: int
