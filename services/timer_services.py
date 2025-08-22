import time
import threading
from interfaces.timer_interface import TimerInterface

class TimerService(TimerInterface):
    def __init__(self, duration: int, callback=None):
        """
        duration: study duration in seconds
        callback: function to call when timer finishes
        """
        self.duration = duration
        self.callback = callback
        self._running = False
        self._thread = None

    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._run)
            self._thread.start()

    def _run(self):
        time.sleep(self.duration)
        if self._running and self.callback:
            self.callback()

    def stop(self):
        self._running = False
