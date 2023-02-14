from datetime import datetime
from pydantic import BaseModel

class MagicLinkTokenPayload(BaseModel):
    exp: datetime
    user_id: int

class MagicLink(BaseModel):
    url: str
    token: str