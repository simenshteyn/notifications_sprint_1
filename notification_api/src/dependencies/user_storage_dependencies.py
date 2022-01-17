from services.user import BaseUserService

user_service: BaseUserService | None = None


def get_user_service() -> BaseUserService | None:
    return user_service() if user_service else None
