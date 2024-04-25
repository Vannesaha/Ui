# menu_frame.py

import tkinter as tk

MENU_FRAME_TITLE = "Valikko"


def create_menu_frame(root):
    """Create the menu frame and its components."""
    menu_frame = tk.Frame(root, borderwidth=2, relief="solid")

    # Create a title label for the frame
    menu_frame_title = tk.Label(menu_frame, text=MENU_FRAME_TITLE, font=("Arial", 16))
    menu_frame_title.pack(anchor="center", padx=10, pady=10)  # Add padding to the title

    # Configure menu_frame to fill the whole column and stick to the top
    menu_frame.pack(fill="both", expand=True, side="left")

    return menu_frame  # Return the menu_frame object
