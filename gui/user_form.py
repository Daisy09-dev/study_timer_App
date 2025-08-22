import customtkinter as ctk
import re
from tkinter import messagebox


class UserForm(ctk.CTkFrame):
    def __init__(self, parent, on_submit_callback):
        super().__init__(parent, corner_radius=15)
        self.on_submit_callback = on_submit_callback

        # Counter for invalid duration attempts
        self.duration_invalid_count = 0
        self.max_invalid_attempts = 3

        #Name Section
        self.label_name = ctk.CTkLabel(self, text="Enter your name:", font=("Helvetica", 14))
        self.label_name.pack(anchor="w", pady=(10, 2), padx=20)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Your name", corner_radius=15, border_width=2)
        self.name_entry.pack(pady=(0, 2), padx=20, fill="x")
        self.name_entry.bind("<KeyRelease>", self.live_validate_name)

        self.name_error = ctk.CTkLabel(self, text="", text_color="red", font=("Helvetica", 11))
        self.name_error.pack(anchor="w", pady=(0, 8), padx=22)

        # === Duration Section ===
        self.label_duration = ctk.CTkLabel(self, text="Study duration (minutes):", font=("Helvetica", 14))
        self.label_duration.pack(anchor="w", pady=(0, 2), padx=20)

        self.duration_entry = ctk.CTkEntry(self, placeholder_text="Enter minutes (e.g. 25)", corner_radius=15, border_width=2)
        self.duration_entry.pack(pady=(0, 2), padx=20, fill="x")
        self.duration_entry.bind("<KeyRelease>", self.live_validate_duration)

        self.duration_error = ctk.CTkLabel(self, text="", text_color="red", font=("Helvetica", 11))
        self.duration_error.pack(anchor="w", pady=(0, 12), padx=22)

        # === Submit Button ===
        self.submit_btn = ctk.CTkButton(self, text="Start", font=("Helvetica", 14), command=self.submit, corner_radius=15)
        self.submit_btn.pack(pady=10)
        self.submit_btn.configure(state="disabled")  # initially disabled

     #Live Validation
    def live_validate_name(self, event=None):
        self.capitalize_name()  # Capitalize name on entry
        text = self.name_entry.get().strip()
        if text == "":
            self.name_entry.configure(border_color="gray")
            self.name_error.configure(text="")
        elif re.match(r"^[A-Za-z ]+$", text):
            self.name_entry.configure(border_color="green")
            self.name_error.configure(text="")
        else:
            self.name_entry.configure(border_color="red")
            self.name_error.configure(text="❌ Only letters and spaces allowed")

        self.update_button_state()

    def live_validate_duration(self, event=None):
        text = self.duration_entry.get().strip()

        if text == "":
            # Empty input
            self.duration_entry.configure(border_color="gray")
            self.duration_error.configure(text="")
        elif text.isdigit() and int(text) > 0:
            # Positive whole number
            if len(text) >= 4:  # check character count
                self.duration_entry.configure(border_color="red")
                self.duration_error.configure(text="❌ Wala nani kaon kaon, tuon lang!")
            else:
                self.duration_entry.configure(border_color="green")
                self.duration_error.configure(text="")
        elif text.isalpha():
            # Letters only
            self.duration_entry.configure(border_color="red")
            self.duration_error.configure(text="❌ Invalid input! Only whole numbers allowed")
        else:
            # Special characters or other invalid input
            self.duration_entry.configure(border_color="red")
            self.duration_error.configure(text="❌ Invalid input! Only whole numbers allowed")

        self.update_button_state()
        
        # Capitalize name on entry
    def capitalize_name(self, event=None):
        """Capitalize the first letter of each word, but keep spaces intact"""
        current_text = self.name_entry.get()
        new_text = ""
        i = 0
        while i < len(current_text):
            if current_text[i].isalpha():
                # Capitalize first letter of a word
                start = i
                while i < len(current_text) and current_text[i].isalpha():
                    i += 1
                word = current_text[start:i]
                new_text += word.capitalize()
            else:
                # Keep non-letter character (like spaces) as-is
                new_text += current_text[i]
                i += 1

        # Update entry without moving the cursor
        cursor_pos = self.name_entry.index("insert")
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, new_text)
        self.name_entry.icursor(cursor_pos)

    #Enable/Disable Button
    def update_button_state(self):
        name_valid = bool(re.match(r"^[A-Za-z ]+$", self.name_entry.get().strip()))
        duration_valid = self.duration_entry.get().isdigit() and int(self.duration_entry.get()) > 0
        self.submit_btn.configure(state="normal" if name_valid and duration_valid else "disabled")

    #Submit
    def submit(self):
        name = self.name_entry.get().strip()
        duration_str = self.duration_entry.get().strip()

        if not re.match(r"^[A-Za-z ]+$", name):
            messagebox.showerror("Invalid Input", "Name must contain only letters and spaces.")
            return

        if not duration_str.isdigit() or int(duration_str) <= 0:
            messagebox.showerror("Invalid Input", "Duration must be a positive whole number.")
            return

        duration = int(duration_str)
        self.on_submit_callback(name, duration)

        # Reset fields and counters
        self.name_entry.delete(0, 'end')
        self.duration_entry.delete(0, 'end')
        self.name_entry.configure(border_color="gray")
        self.duration_entry.configure(border_color="gray")
        self.name_error.configure(text="")
        self.duration_error.configure(text="")
        self.duration_invalid_count = 0
        self.submit_btn.configure(state="disabled")
