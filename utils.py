import os


def is_admin(user_id: int) -> bool:
    admin_ids = {
        os.getenv("my_admins"),
        os.getenv("my_admins2")
    }
    return str(user_id) in admin_ids
