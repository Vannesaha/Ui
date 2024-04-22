# Update the text and color of a label based on a status


def update_status(label, status):
    # Map statuses to colors
    status_colors = {
        "online": "green",
        "offline": "red",
        "error": "orange",  # not in use
        "maintenance": "yellow",  # not in use
        # Add more statuses and colors as needed
    }

    # Get the color for the status, or black if the status is not in the dictionary
    color = status_colors.get(status.lower(), "black")

    # Update the text and color of the label
    base_text = label.cget("text").split(":")[0]  # Get the base text before the colon
    label.config(text=f"{base_text}: {status}", fg=color)
