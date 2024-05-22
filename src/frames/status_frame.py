# status_frame.py

import tkinter as tk

STATUS_LABELS = {
    "hydraulic": "Hydraulic Status: ",
    "embedded": "Embedded Device Status: ",
    # Add more labels here
}

STATUS_FRAME_TITLE = "Laitteiden tila"


def create_status_frame(root, device_labels):
    """Create the status frame and its components."""
    status_frame = tk.Frame(root, borderwidth=0, relief="solid", bg="#378AEC")

    # Create a title label for the frame
    status_frame_title = tk.Label(
        status_frame,
        text=STATUS_FRAME_TITLE,
        font=("Inter Medium", 20),
        bg="#378AEC",  # color for menu text backround
        fg="#D9DAF9",  # color for menu texts
    )
    status_frame_title.pack(fill="x", padx=10, pady=10)

    # Create labels and map device IDs to status labels
    for device_id, label_text in STATUS_LABELS.items():
        label = tk.Label(status_frame, text=label_text, bg="#378AEC", fg="#D9DAF9")
        label.pack()
        device_labels[device_id] = label

    return status_frame  # Return the status frame
