# menu_frame.py

import tkinter as tk

MENU_FRAME_TITLE = "Valikko"


def create_menu_frame(root):
    """Create the menu frame and its components."""
    menu_frame = tk.Frame(
        root, borderwidth=2, relief="solid", bg="#0109D4"
    )  # bg = color for menu background

    # Create a title label for the frame
    menu_frame_title = tk.Label(
        menu_frame,
        text=MENU_FRAME_TITLE,
        font=("Inter Medium", 20),
        bg="#0109D4",  # color for menu text background
        fg="#D9DAF9",  # color for menu texts
    )
    menu_frame_title.grid(row=0, column=0, pady=(5, 0), padx=5)

    # Place the menu_frame_title in the center horizontally
    menu_frame.grid_rowconfigure(0, weight=0)
    menu_frame.grid_columnconfigure(0, weight=1)

    # # Create 'Jatka' button
    # continue_button = tk.Button(
    #     menu_frame, text="Jatka", command=lambda: print("Jatka clicked")
    # )
    # continue_button.grid(row=2, column=1, padx=(0, 10), pady=10, sticky="nsew")

    # # Create 'Takaisin' button
    # back_button = tk.Button(
    #     menu_frame, text="Takaisin", command=lambda: print("Takaisin clicked")
    # )
    # back_button.grid(row=2, column=0, padx=(10, 0), pady=10, sticky="nsew")

    return menu_frame  # Return the menu_frame object
