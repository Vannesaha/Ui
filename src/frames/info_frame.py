# info_frame.py

import tkinter as tk
from src.utils.button_manager import ButtonManager

# OK_BUTTON_TEXT = "Jatka"
# BACK_BUTTON_TEXT = "Takaisin"
# DELETE_BUTTON_TEXT = "Poista"
INFO_FRAME_TITLE = "Info"


def create_info_frame():
    info_frame = tk.Frame(
        borderwidth=2, relief="solid", bg="#0109D4"
    )  # Create a frame with a border and a solid relief effect with a blue background

    # Create a title for the info_frame
    info_frame_title = tk.Label(info_frame, text=INFO_FRAME_TITLE, bg="#0109D4")
    info_frame_title.grid(
        row=0, column=0, columnspan=5, sticky="ew"
    )  # Title is centered in the frame and spans all columns of the frame

    # Create a ButtonManager for the
    # button_manager = ButtonManager(navigation_frame)

    # Create buttons in the other_frame using grid method
    # button_texts = [OK_BUTTON_TEXT, BACK_BUTTON_TEXT, DELETE_BUTTON_TEXT]
    # button_commands = [ok_button_command, back_button_command, delete_button_command]

    # for i in range(3):
    #     button = button_manager.create_other_buttons(
    #         button_texts[i], button_commands[i]
    #     )
    #     button.grid(row=1, column=i, padx=5, pady=5, sticky="ew")
    #     button.config(anchor="center")

    #     # Configure the columns to have equal weight
    #     navigation_frame.grid_columnconfigure(i, weight=1)

    # # Bind keyboard buttons to the button commands
    # root.bind("o", ok_button_command)
    # root.bind("b", back_button_command)
    # root.bind("d", delete_button_command)

    return info_frame
