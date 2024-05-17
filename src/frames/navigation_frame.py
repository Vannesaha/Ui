import tkinter as tk


def create_navigation_frame(
    root, up_command, down_command, left_command, right_command
):
    navigation_frame = tk.Frame(root, borderwidth=2, relief="solid", bg="#0109D4")

    # Configure the frame to have 3 rows and 3 columns
    for i in range(3):
        navigation_frame.grid_rowconfigure(i, weight=1)
        navigation_frame.grid_columnconfigure(i, weight=1)

    # Create direction buttons and place them in the respective positions
    up_button = tk.Button(
        navigation_frame,
        text="Ylös",
        command=up_command,
        width=10,
        highlightbackground="#0109D4",
        bg="#378AEC",
        borderwidth=2,
        relief="solid",
    )
    down_button = tk.Button(
        navigation_frame,
        text="Alas",
        command=down_command,
        width=10,
        highlightbackground="#0109D4",
        bg="#378AEC",
        borderwidth=2,
        relief="solid",
    )
    left_button = tk.Button(
        navigation_frame,
        text="Vasen",
        command=left_command,
        width=10,
        highlightbackground="#0109D4",
        bg="#378AEC",
        borderwidth=2,
        relief="solid",
    )
    right_button = tk.Button(
        navigation_frame,
        text="Oikea",
        command=right_command,
        width=10,
        highlightbackground="#0109D4",
        bg="#378AEC",
        borderwidth=2,
        relief="solid",
    )

    # Place buttons in the grid
    up_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")  # Top (up)
    left_button.grid(row=1, column=0, padx=5, pady=5, sticky="ns")  # Left
    right_button.grid(row=1, column=2, padx=5, pady=5, sticky="ns")  # Right
    down_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")  # Bottom (down)

    return navigation_frame
