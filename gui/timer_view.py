import customtkinter as ctk
import datetime
from services.timer_services import TimerService
from services.notification_service import NotificationService

class TimerView(ctk.CTkFrame):
    def __init__(self, parent, user_name, duration_minutes):
        super().__init__(parent)
        self.user_name = user_name
        self.duration_seconds = duration_minutes * 60
        self.remaining = self.duration_seconds
        self.timer_service = None

        # Label for user
        self.label = ctk.CTkLabel(self, text=f"{self.user_name}, Ready to Study!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Timer display
        self.time_label = ctk.CTkLabel(self, text=self.format_time(self.remaining), font=("Helvetica", 28))
        self.time_label.pack(pady=10)

        # Start and Stop Buttons
        self.start_btn = ctk.CTkButton(self, text="▶ Start Timer", command=self.start_timer, corner_radius=15)
        self.start_btn.pack(side="left", padx=15, pady=20)

        self.stop_btn = ctk.CTkButton(self, text="⏹ Stop Timer", command=self.stop_timer, corner_radius=15, fg_color="red")
        self.stop_btn.pack(side="right", padx=15, pady=20)

    def format_time(self, seconds):
        """ Format as HH:MM:SS """
        return str(datetime.timedelta(seconds=seconds))

    def update_display(self):
        self.time_label.configure(text=self.format_time(self.remaining))
        if self.remaining > 0 and self.timer_service and self.timer_service._running:
            self.remaining -= 1
            self.after(1000, self.update_display)
        elif self.remaining == 0:
            notifier = NotificationService()
            notifier.notify("⏰ Time’s up! Take a break!")

    def start_timer(self):
        if not self.timer_service:
            self.timer_service = TimerService(self.duration_seconds, self.timer_finished)
        self.remaining = self.duration_seconds
        self.timer_service.start()
        self.update_display()
        self.label.configure(text=f"{self.user_name}, Stay Focused!")

    def stop_timer(self):
        if self.timer_service:
            self.timer_service.stop()
            self.label.configure(text="⏹ Timer Stopped.")

    def timer_finished(self):
        self.label.configure(text="✅ Session Completed!")
