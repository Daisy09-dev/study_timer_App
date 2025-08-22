from interfaces.notifier_interface import NotifierInterface
import tkinter.messagebox as msg

class NotificationService(NotifierInterface):
    def notify(self, message: str):
        """Show a notification (basic Tkinter messagebox)."""
        msg.showinfo("Study Timer", message)
        print(f"Notification: {message}")