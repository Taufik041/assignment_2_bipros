from pydantic import BaseModel
from enum import Enum

class employee_data(BaseModel):
    id: int = None
    name: str
    company: str
    
class sort_field(str, Enum):
    id: str = "id"
    name: str = "name"
    company: str = "company"