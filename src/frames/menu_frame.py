# menu_frame.py

import tkinter as tk

MENU_FRAME_TITLE = "Valikko"
BUTTON_OK_TEXT = "Jatka"
BUTTON_BACK_TEXT = "Takaisin"


def create_menu_frame(root, ok_button_command, back_button_command):
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

    # Configure row and column weights to center the title and buttons
    menu_frame.grid_rowconfigure(0, weight=0)
    menu_frame.grid_rowconfigure(1, weight=0)  # Spacer row to push buttons to bottom
    menu_frame.grid_rowconfigure(2, weight=1)
    menu_frame.grid_rowconfigure(3, weight=0)
    menu_frame.grid_columnconfigure(0, weight=1)

    # Create 'Jatka' button
    continue_button = tk.Button(
        menu_frame,
        text=BUTTON_OK_TEXT,
        command=ok_button_command,
    )
    continue_button.grid(row=3, column=0, padx=(5, 5), pady=(1, 5), sticky="e")
    continue_button.configure(
        width=10,
        highlightbackground="#0109D4",
        bg="#378AEC",
        borderwidth=2,
        relief="solid",
    )  # Määritä taustaväri

    # Create 'Takaisin' button
    back_button = tk.Button(
        menu_frame,
        text=BUTTON_BACK_TEXT,
        command=back_button_command,
    )
    back_button.grid(row=3, column=0, padx=(5, 5), pady=(1, 5), sticky="w")
    back_button.configure(
        width=10,
        highlightbackground="#0109D4",
        bg="#378AEC",
        borderwidth=2,
        relief="solid",
    )  # Määritä taustaväri

    # Bind keyboard buttons to the button commands
    root.bind("o", ok_button_command)
    root.bind("b", back_button_command)

    return menu_frame  # Return the menu_frame object
