from abc import ABC, abstractmethod


class EspBase(ABC):
    """Interface for ESP."""

    @abstractmethod
    def check_user_email(self):
        pass

    @abstractmethod
    def add_user_email(self):
        pass
