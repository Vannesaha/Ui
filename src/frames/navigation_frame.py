# other_frame.py
import tkinter as tk
from src.utils.button_manager import ButtonManager

OK_BUTTON_TEXT = "OK"
BACK_BUTTON_TEXT = "Back"
DELETE_BUTTON_TEXT = "Delete"
OTHER_FRAME_TITLE = "Other Frame Title"


def create_navigation_frame(
    root, ok_button_command, back_button_command, delete_button_command
):
    other_frame = tk.Frame(root, borderwidth=2, relief="solid")

    # Create a title for the other_frame
    other_frame_title = tk.Label(other_frame, text=OTHER_FRAME_TITLE)
    other_frame_title.grid(row=0, column=0, columnspan=5, sticky="ew")

    # Create a ButtonManager for the other_frame
    button_manager = ButtonManager(other_frame)

    # Create buttons in the other_frame using grid method
    button_texts = [OK_BUTTON_TEXT, BACK_BUTTON_TEXT, DELETE_BUTTON_TEXT]
    button_commands = [ok_button_command, back_button_command, delete_button_command]

    for i in range(3):
        button = button_manager.create_other_buttons(
            button_texts[i], button_commands[i]
        )
        button.grid(row=1, column=i, padx=5, pady=5, sticky="ew")
        button.config(anchor="center")

        # Configure the columns to have equal weight
        other_frame.grid_columnconfigure(i, weight=1)

    # Bind keyboard buttons to the button commands
    root.bind("o", ok_button_command)
    root.bind("b", back_button_command)
    root.bind("d", delete_button_command)

    return other_frame
