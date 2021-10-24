from typing import List

from .abc import EspBase


class Esp(EspBase):
    """Mock for esp."""

    def __init__(self, data: List[str] = None) -> None:
        self.data = data or []

    def check_user_email(self, email: str) -> bool:
        if email in self.data:
            return True
        return False

    def add_user_email(self, email: str) -> None:
        self.data.append(email)


emails = ["user@example.com", "user2@example.com"]
esp = Esp(data=emails)
