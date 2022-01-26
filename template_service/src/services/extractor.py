from functools import lru_cache
from uuid import UUID

from faker import Faker

from models.user import User


class ExtractorService:
    """Class to extract data from outer services, mocking fake data now."""

    async def get_user_data(self, user_id: UUID) -> User:
        fake = Faker()
        result = User(
            user_id=user_id,
            user_name=fake.first_name(),
            user_last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            telegram_user_name=fake.domain_word(),
            location=fake.city(),
            birthdate=fake.date_of_birth(),
        )
        return result


@lru_cache()
def get_extractor_service() -> ExtractorService:
    return ExtractorService()
