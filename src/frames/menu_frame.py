# menu_frame.py


import tkinter as tk

MENU_FRAME_TITLE = "Valikko"


def create_menu_frame(root):
    """Create the menu frame and its components."""
    menu_frame = tk.Frame(root, borderwidth=0, relief="ridge", bg="#0109D4")

    # Create a title label for the frame
    menu_frame_title = tk.Label(
        menu_frame,
        text=MENU_FRAME_TITLE,
        font=("Inter Medium", 20),
        bg="#0109D4",  # Match the background color
        fg="#D9DAF9",
    )
    menu_frame_title.pack(anchor="center")  # Center the title

    # Configure menu_frame to fill the whole column and stick to the top
    menu_frame.pack(fill="both", expand=True, side="left", padx=50, pady=0)

    return menu_frame  # Return the menu_frame object
