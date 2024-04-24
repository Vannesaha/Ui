# window_utils.py


def set_window_size(window, max_width=1024, max_height=600):
    # Get the screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # If the screen size is smaller than the maximum size, set the window size to the screen size
    if screen_width < max_width and screen_height < max_height:
        window.geometry(f"{screen_width}x{screen_height}")
    else:
        # If the screen size is larger than the maximum size, set the window size to the maximum size
        window.geometry(f"{max_width}x{max_height}")
