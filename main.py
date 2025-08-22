import os
from PIL import Image
import customtkinter as ctk
from gui.main_window import MainWindow
from database.connection import DatabaseConnection


def main():
    # Initialize database
    db = DatabaseConnection()
    db.initialize()

    # Start GUI
    ctk.set_appearance_mode("dark")   # "light" or "dark"
    ctk.set_default_color_theme("dark-blue")  # "blue", "green", "dark-blue"

    root = ctk.CTk()
    root.title("Study Timer App")
    root.geometry("400x400")
    root.resizable(False, False)  # Disable resizing


    # Dynamically load background image
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # absolute path
    image_path = os.path.join(BASE_DIR, "assets", "study_timer.jpg")
    print(f"[DEBUG] Looking for image at: {image_path}")  # debug line

    if not os.path.exists(image_path):
        print(f"[ERROR] Image not found at {image_path}")
        return

    # Use CTkImage (handles scaling + DPI correctly)
    bg_image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(400, 400))

    # Background image on CTkLabel
    background_label = ctk.CTkLabel(root, text="", image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Main window content (above background)
    app = MainWindow(root)
    app.place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()


if __name__ == "__main__":
    main()
