def handle_notification(data):
    ntype = data["type"]
    message = data["message"]
    user_id = data["user_id"]

    if ntype == "email":
        print(f"[Email] To user {user_id}: {message}")
    elif ntype == "sms":
        print(f"[SMS] To user {user_id}: {message}")
    elif ntype == "inapp":
        print(f"[InApp] Notification to user {user_id}: {message}")
