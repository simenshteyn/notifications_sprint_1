import uuid
from typing import List, Optional

import requests
from airflow.operators.branch_operator import BaseBranchOperator
from pydantic import BaseSettings, Field


class BirthdayCheckOperator(BaseBranchOperator):
    def __init__(self, correct_way: str, wrong_way: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.correct_way = correct_way
        self.wrong_way = wrong_way
        self.host: str = Field("http://localhost:8001", env="USER_DB_HOST")
        self.endpoint: str = Field("/api/v1/user/today-birthdate", env="BIRTHDATE_ENDPOINT")

        self.notifications_file = Field("/tmp/notification", env="NOTIFICATIONS_FILE")

    def _get_birthdays(self) -> Optional[str]:
        response = requests.get(f"{self.host}{self.endpoint}")
        return response.json()["users_birthdays"] or None

    def choose_branch(self, *args, **kwargs):
        birthdays = self._get_birthdays()
        if birthdays is None:
            return [self.wrong_way]

        with open(self.notifications_file, mode="w", encoding="utf8") as file:
            file.write("\n".join(birthdays))
        return [self.correct_way]
