from abc import ABC, abstractmethod

class TimerInterface(ABC):
    @abstractmethod
    def start(self):
        """Start the timer"""
        pass

    @abstractmethod
    def stop(self):
        """Stop the timer"""
        pass
