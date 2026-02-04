from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WrapperRegSecListUsers(BaseModel):
    codEmpresa: Optional[str] = None
    codSucursal: Optional[str] = None
    authToken: Optional[str] = None