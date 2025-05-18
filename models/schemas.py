from pydantic import BaseModel
from typing import Literal

class NotificationRequest(BaseModel):
    user_id: int
    type: Literal["email", "sms", "inapp"]
    message: str

class NotificationResponse(BaseModel):
    status: str
    detail: str
