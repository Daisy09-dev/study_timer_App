from abc import ABC, abstractmethod

class NotifierInterface(ABC):
    @abstractmethod
    def notify(self, message: str):
        """Notify user with a message"""
        pass
