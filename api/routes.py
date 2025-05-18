from fastapi import APIRouter
from app.models.schemas import NotificationRequest, NotificationResponse
from app.services.producer import send_to_kafka

router = APIRouter()

@router.post("/notifications", response_model=NotificationResponse)
def send_notification(request: NotificationRequest):
    send_to_kafka("notifications", request.dict())
    return {"status": "queued", "detail": "Notification queued for processing."}

@router.get("/users/{user_id}/notifications")
def get_notifications(user_id: int):
    # Dummy response for now
    return {"user_id": user_id, "notifications": ["In-App message example"]}
